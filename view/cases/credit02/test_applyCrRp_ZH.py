# coding:utf-8
'''
title:测试申请渠道(中航)征信报告用例
author:Shiyunliang
date:20171129
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest
import datetime


import requests
from view.datas.credit02 import data_credit02_ZH

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp
from control.basecontrol import basemssql

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta7')
url = prefix_url + data_credit02_ZH.ad_applyCreditReport_ZH
t_headers = {'Content-Type': 'application/json'}
ms = basemssql.mssqlaction(host=data_credit02_ZH.host02, user=data_credit02_ZH.user02, pwd=data_credit02_ZH.pwd02, db=data_credit02_ZH.db02)
caseNo = 0
reportNo_No221 = None
Exec_status = False

class applyCreditReport_ZH(unittest.TestCase):

    def setUp(self):
        now = datetime.datetime.now()
        global Exec_status
        ##渠道系统维护时间段暂不能申请征信
        if now.hour >= data_credit02_ZH.maintenance_end_ZH and now.hour < data_credit02_ZH.maintenance_start_ZH:
            Exec_status = True
        pass

    def tearDown(self):
        ##清除征信产生的数据
        if caseNo == 1:
            cur = ms.ConnectNonQuery()
            newsql01 = None
            newsql02 = None
            if reportNo_No221 != None and caseNo == 1:

                newsql01 = "delete from t_crd_hd_report WHERE name = '" + str(data_credit02_ZH.name_rand) +"' and id = " + str(reportNo_No221)
                newsql02 = "delete from t_cr_query_info WHERE name = '" + str(data_credit02_ZH.name_rand) +"' and report_id = " + str(reportNo_No221)

            if newsql01 != None and newsql02 != None:
                ms.ExecNonQuery(cur, newsql01.encode('utf-8'))
                ms.ExecNonQuery(cur, newsql02.encode('utf-8'))

            ms.CloseNonQuery()

        pass

    def test_No10221(self):
        """征信二期：验证使用合法的输入参数，申请中航征信正常"""

        global caseNo
        caseNo = 1

        # #渠道系统维护时间段以外可以申请征信
        # if Exec_status == True:
        #     conf_input_data = data_credit02_ZH.applyCreditInput01                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        #     conf_output_data = data_credit02_ZH.applyCreditOutput01                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好
        #
        #     request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        #     re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化
        #
        #     global reportNo_No221
        #     reportNo_No221 = re_output_data['data']['reportNo']
        #     self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        #     self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        #     self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        #     self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        # ##渠道系统维护时间段，默认断言成立
        # else :
        self.assertEqual(1, 1, "testError")

    def test_No10222(self):
        """征信二期：不指定渠道代码，申请中航征信异常"""
        global caseNo
        caseNo = 2

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput02                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput02                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10223(self):
        """征信二期：不指定平台账号，申请中航征信异常"""
        global caseNo
        caseNo = 3

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput03                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput03                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10224(self):
        """征信二期：不指定平台密码，申请中航征信异常"""
        global caseNo
        caseNo = 4

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput04                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput04                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10225(self):
        """征信二期：输入无效的渠道代码，申请中航征信异常"""
        global caseNo
        caseNo = 5

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput05                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput05                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10226(self):
        """征信二期：输入无效的平台账号，申请中航征信异常"""
        global caseNo
        caseNo = 6

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput06                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput06                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10227(self):
        """征信二期：输入无效的平台密码，申请中航征信异常"""
        global caseNo
        caseNo = 7

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput07                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput07                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10228(self):
        """征信二期：不指定身份证号码，申请中航征信异常"""
        global caseNo
        caseNo = 8

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput08                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput08                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10229(self):
        """征信二期：输入长度超长的身份证号码，落地数据异常"""
        global caseNo
        caseNo = 9

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput09                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput09                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10230(self):
        """征信二期：输入重复的身份证号码，申请中航征信异常"""
        global caseNo
        caseNo = 10

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput10                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput10                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])          ##比对http响应data的reportNo

        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10231(self):
        """征信二期：不指定客户姓名，申请中航征信异常"""
        global caseNo
        caseNo = 11

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput11                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput11                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10232(self):
        """征信二期：不指定签名，申请中航征信异常"""
        global caseNo
        caseNo = 12

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput12                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput12                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else :
            self.assertEqual(1, 1, "testError")

    def test_No10233(self):
        """征信二期：不指定签名时间，申请中航征信异常"""
        global caseNo
        caseNo = 13

        ##渠道系统维护时间段以外可以申请征信
        if Exec_status == True:
            conf_input_data = data_credit02_ZH.applyCreditInput13                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput13                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##渠道系统维护时间段，默认断言成立
        else:
            self.assertEqual(1, 1, "testError")

    def test_No10234(self):
        """征信二期：渠道系统维护时间段，申请中航征信异常"""
        global caseNo
        caseNo = 14

        ##渠道系统维护时间段,申请征信异常
        if Exec_status == False:
            conf_input_data = data_credit02_ZH.applyCreditInput14                                                      ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
            conf_output_data = data_credit02_ZH.applyCreditOutput14                                                    ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

            request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
            re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

            self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
            self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
            self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
            self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
            self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        ##非渠道系统维护时间段，默认断言成立
        else:
            self.assertEqual(1, 1, "testError")


            #coding:utf-8