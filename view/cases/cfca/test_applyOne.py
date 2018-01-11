# coding:utf-8
'''
title:申请合同签章（一个签章/签名）用例
author:Shiyunliang
date:20180103
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest
import time

import requests
from view.datas.cfca import data_applyOne

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp
from control.basecontrol import basemssql

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'serverbeta2_cfca')
url01 = prefix_url + data_applyOne.ad_applyOne
url02 = prefix_url + data_applyOne.ad_retrieve
t_headers = {'Content-Type': 'application/json'}
ms = basemssql.mssqlaction(host=data_applyOne.host, user=data_applyOne.user, pwd=data_applyOne.pwd, db=data_applyOne.db)

applyId_No = 0
is_cleared = 1

def cfca_check(self, conf_output_data, re_output_data, sleeptime):
    ##验证签章状态
    if re_output_data['Status'] == 1:
        ##签章生成成功
        self.assertEqual(re_output_data['Status'], conf_output_data['Status'])  ##比对http响应status
        self.assertEqual(re_output_data['Message'], conf_output_data['Message'])  ##比对http响应msg
    elif re_output_data['Status'] == 99 or re_output_data['Status'] == 3:
        ##签章生成错误
        self.assertEqual(re_output_data['Status'], conf_output_data['Status'],
                         re_output_data['Message'])  ##比对http响应status
    else:
        ##签章生成中或者部分成功时，需要进行DB轮询

        SealApplyId = re_output_data['SealApplyId']

        ##进行DB轮询，验证签章生成状态
        newsql01 = "select status from [dbo].[t_contract_apply] WHERE id = '" + str(SealApplyId) + "'"

        ##进行DB轮询，返回签章完成时间
        newsql02 = "select complete_time, apply_time from [dbo].[t_contract_apply] WHERE id = '" + str(SealApplyId) + "'"

        # DB轮询的签章状态
        status_temp = 0

        i = 0
        while status_temp == 0 and i < data_applyOne.maxjob_cnt:
            i += 1
            # print("第" + str(i) + "次DB轮询!")
            # DB轮询的时间间隔
            time.sleep(sleeptime)
            resList01 = ms.ExecQuery(newsql01)

            for apply_status in resList01:
                # print("apply_status:", apply_status['status'], type(apply_status['status']))
                if apply_status['status'] == 1:
                    status_temp = 1

        if status_temp == 1:
            ##计算签章完成时间
            resList02 = ms.ExecQuery(newsql02)

            for finsh_time in resList02:
                # print("complete_time:", finsh_time['complete_time'], type(finsh_time['complete_time']))
                # print("apply_time:", finsh_time['apply_time'], type(finsh_time['apply_time']))
                t = finsh_time['complete_time'] - finsh_time['apply_time']

            print("第" + str(i) + "次DB轮询，返回签章成功，完成时间：" + str(t))

        t_str = sleeptime * data_applyOne.maxjob_cnt

        self.assertEqual(apply_status['status'], conf_output_data['Status'],
                         "进行了" + str(data_applyOne.maxjob_cnt) + "次DB轮询，仍然返回签章失败，总共耗时：" + str(t_str) + "秒")  ##比对http响应data的apply_status


class applyOne(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ##清除签章产生的数据

        ##判断是否需要清除签章数据
        if is_cleared == 1:
            cur = ms.ConnectNonQuery()
            newsql03 = ""
            newsql04 = ""
            newsql05 = ""
            newsql06 = ""
            if applyId_No != 0:
                newsql03 = "delete from [dbo].[t_contract_apply] WHERE id = " + str(applyId_No)
                newsql04 = "delete from [dbo].[t_contract_apply_detail] WHERE apply_id = " + str(applyId_No)
                newsql05 = "delete from [dbo].[t_contract] WHERE apply_id = " + str(applyId_No)
                newsql06 = "delete from [dbo].[t_sys_error_message] WHERE main_data like 'applyId=" + str(applyId_No) + "%'"

            if newsql03 != "" and newsql04 != "" and newsql05 != "" and newsql06 != "" :
                ms.ExecNonQuery(cur, newsql03.encode('utf-8'))
                ms.ExecNonQuery(cur, newsql04.encode('utf-8'))
                ms.ExecNonQuery(cur, newsql05.encode('utf-8'))
                ms.ExecNonQuery(cur, newsql06.encode('utf-8'))

            ms.CloseNonQuery()
        pass

    def test_No10511 (self):
        """签章二期（单个签章签名）：异步请求申请10个合同签章/签名，返回签章生成中的话，会轮询数据库签章状态，直到签章成功，超过最大轮询次数，则签章失败"""

        conf_input_data = data_applyOne.applyOneInput01                                                ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput01                                              ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url01, data=json.dumps(conf_input_data), headers=t_headers)               ##请求签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        ##获取签章申请ID
        global applyId_No
        applyId_No = re_output_data['SealApplyId']

        ##设置DB轮询间隔时间
        sleeptime = 120

        ##验证签章状态
        cfca_check(self, conf_output_data, re_output_data, sleeptime)

    def test_No10512(self):
        """签章二期（单个签章签名）：异步请求申请1个合同签章/签名，返回签章生成中的话，会轮询数据库签章状态，直到签章成功，超过最大轮询次数，则签章失败"""

        conf_input_data = data_applyOne.applyOneInput02  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput02  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url01, data=json.dumps(conf_input_data), headers=t_headers)  ##请求签章
        re_output_data = request_content.json()  ##把http请求的响应内容进行json格式化

        ##获取签章申请ID
        global applyId_No
        applyId_No = re_output_data['SealApplyId']

        ##设置DB轮询间隔时间
        sleeptime = 20

        ##验证签章状态
        cfca_check(self, conf_output_data, re_output_data, sleeptime)

    def test_No10513(self):
        """签章二期（单个签章签名）：异步请求申请5个合同签章/签名，返回签章生成中的话，会轮询数据库签章状态，直到签章成功，超过最大轮询次数，则签章失败"""

        conf_input_data = data_applyOne.applyOneInput03  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput03  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url01, data=json.dumps(conf_input_data), headers=t_headers)  ##请求签章
        re_output_data = request_content.json()  ##把http请求的响应内容进行json格式化

        ##获取签章申请ID
        global applyId_No
        applyId_No = re_output_data['SealApplyId']

        ##设置DB轮询间隔时间
        sleeptime = 75

        ##验证签章状态
        cfca_check(self, conf_output_data, re_output_data, sleeptime)

    def test_No10514(self):
        """签章二期（单个签章签名）：异步请求申请20个合同签章/签名，返回签章生成中的话，会轮询数据库签章状态，直到签章成功，超过最大轮询次数，则签章失败"""

        conf_input_data = data_applyOne.applyOneInput04  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput04  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url01, data=json.dumps(conf_input_data), headers=t_headers)  ##请求签章
        re_output_data = request_content.json()  ##把http请求的响应内容进行json格式化

        ##获取签章申请ID
        global applyId_No
        applyId_No = re_output_data['SealApplyId']

        ##不需要清除签章申请数据，为下一个接口提供查询
        global is_cleared
        is_cleared = 0

        ##设置DB轮询间隔时间
        sleeptime = 120

        ##验证签章状态
        cfca_check(self, conf_output_data, re_output_data, sleeptime)

    def test_No10515(self):
        """签章二期（单个签章签名）：按签章申请ID(CaseNo10514)，取得20个合同的申请结果"""

        conf_input_data = data_applyOne.applyOneInput05  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput05  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        ##获取CaseNo10514的签章申请ID
        conf_input_data['SealApplyId'] = str(applyId_No)

        request_content = requests.post(url02, data=json.dumps(conf_input_data), headers=t_headers)             ##请求签章
        re_output_data = request_content.json()                                                                 ##把http请求的响应内容进行json格式化

        ##需要清除CaseNo10514的签章申请数据
        global is_cleared
        is_cleared = 1

        self.assertEqual(re_output_data['Status'], conf_output_data['Status'], re_output_data['Message'])    ##比对http响应status
        self.assertEqual(re_output_data['Message'], conf_output_data['Message'], re_output_data['Message'])  ##比对http响应msg
        self.assertEqual(re_output_data['SealApplyCount'], conf_output_data['SealApplyCount'])              ##比对http响应SealApplyCount
        self.assertEqual(re_output_data['SuccessCount'], conf_output_data['SuccessCount'])                   ##比对http响应SuccessCount

    def test_No10516(self):
        """签章二期（单个签章签名）：同步请求申请1个合同签章/签名，返回签章生成状态，不会轮询数据库"""

        conf_input_data = data_applyOne.applyOneInput06  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput06  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url01, data=json.dumps(conf_input_data), headers=t_headers)  ##请求签章
        re_output_data = request_content.json()  ##把http请求的响应内容进行json格式化

        ##获取签章申请ID
        global applyId_No
        applyId_No = re_output_data['SealApplyId']

        ##不需要清除签章申请数据，为下一个接口提供查询
        global is_cleared
        is_cleared = 0

        self.assertEqual(re_output_data['Status'], conf_output_data['Status'], re_output_data['Message'])  ##比对http响应status
        self.assertEqual(re_output_data['Message'], conf_output_data['Message'], re_output_data['Message'])  ##比对http响应msg

    def test_No10517(self):
        """签章二期（单个签章签名）：按签章申请ID(CaseNo10516)，取得1个合同的申请结果"""

        conf_input_data = data_applyOne.applyOneInput07  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyOne.applyOneOutput07  ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        ##获取CaseNo10516的签章申请ID
        conf_input_data['SealApplyId'] = str(applyId_No)

        request_content = requests.post(url02, data=json.dumps(conf_input_data), headers=t_headers)             ##请求签章
        re_output_data = request_content.json()                                                                 ##把http请求的响应内容进行json格式化

        ##需要清除CaseNo10516的签章申请数据
        global is_cleared
        is_cleared = 1

        ##设置DB轮询间隔时间
        sleeptime = 15

        ##验证签章状态
        cfca_check(self, conf_output_data, re_output_data, sleeptime)

            #coding:utf-8