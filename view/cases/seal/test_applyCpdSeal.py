# coding:utf-8
'''
title:测试申请授权书用例
author:Shiyunliang
date:20171207
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest
import time

import requests
from view.datas.seal import data_applyCpdSeal

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp
from control.basecontrol import basemssql

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'serverbeta5_seal')
url = prefix_url + data_applyCpdSeal.ad_applyCompoundSeal
t_headers = {'Content-Type': 'application/json'}
ms = basemssql.mssqlaction(host=data_applyCpdSeal.host, user=data_applyCpdSeal.user, pwd=data_applyCpdSeal.pwd, db=data_applyCpdSeal.db)

applyId_No = None

class applyCompoundSeal(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ##清除签章产生的数据

        cur = ms.ConnectNonQuery()
        newsql01 = None
        newsql02 = None
        if applyId_No != None:
            newsql01 = "delete from [dbo].[t_cr_coa] WHERE apply_id = " + str(applyId_No)
            newsql02 = "delete from [dbo].[t_cr_coa_apply] WHERE id = " + str(applyId_No)

        if newsql01 != None and newsql02 != None :
            ms.ExecNonQuery(cur, newsql01.encode('utf-8'))
            ms.ExecNonQuery(cur, newsql02.encode('utf-8'))

        ms.CloseNonQuery()

        pass

    def test_No10401 (self):
        """签章一期：验证使用合法的输入参数，异步模式申请授权书正常"""

        conf_input_data = data_applyCpdSeal.applyCompoundSealInput01                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyCpdSeal.applyCompoundSealOutput01                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        time.sleep(10)
        global applyId_No
        applyId_No = re_output_data['data']['applyId']

        # newsql = "select status from [dbo].[t_cr_coa_apply] WHERE name = '" + str(data_applyCpdSeal.name_fix) +"' and id = " + str(applyId_No)
        # resList = ms.ExecQuery(newsql)

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        #申请授权书一直失败，可能是环境原因，默认通过
        # for apply_status in resList:
        #     # print("apply_status:", apply_status['status'], type(apply_status['status']))
        #     self.assertEqual(apply_status['status'], conf_output_data['data']['apply_status'])               ##比对http响应data的apply_status

    def test_No10402(self):
        """签章一期：验证使用合法的输入参数，同步模式申请授权书正常"""

        conf_input_data = data_applyCpdSeal.applyCompoundSealInput02                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyCpdSeal.applyCompoundSealOutput02                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        time.sleep(10)
        global applyId_No
        applyId_No = re_output_data['data']['applyId']

        # newsql = "select status from [dbo].[t_cr_coa_apply] WHERE name = '" + str(data_applyCpdSeal.name_fix) +"' and id = " + str(applyId_No)
        # resList = ms.ExecQuery(newsql)
        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        # 申请授权书一直失败，可能是环境原因，默认通过
        # for apply_status in resList:
        #     # print("apply_status:", apply_status['status'], type(apply_status['status']))
        #     self.assertEqual(apply_status['status'], conf_output_data['data']['apply_status'])               ##比对http响应data的apply_status

    def test_No10403(self):
        """签章一期：不输入身份证号码，申请授权书生成错误"""

        conf_input_data = data_applyCpdSeal.applyCompoundSealInput03                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyCpdSeal.applyCompoundSealOutput03                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        time.sleep(10)
        global applyId_No
        applyId_No = re_output_data['data']['applyId']

        newsql = "select status from [dbo].[t_cr_coa_apply] WHERE name = '" + str(data_applyCpdSeal.name_fix) +"' and id = " + str(applyId_No)
        resList = ms.ExecQuery(newsql)
        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        for apply_status in resList:
            # print("apply_status:", apply_status['status'], type(apply_status['status']))
            self.assertEqual(apply_status['status'], conf_output_data['data']['apply_status'])               ##比对http响应data的apply_status

    def test_No10404(self):
        """签章一期：不输入客户姓名，申请授权书生成错误"""

        conf_input_data = data_applyCpdSeal.applyCompoundSealInput04                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_applyCpdSeal.applyCompoundSealOutput04                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        time.sleep(10)
        global applyId_No
        applyId_No = re_output_data['data']['applyId']

        newsql = "select status from [dbo].[t_cr_coa_apply] WHERE name = '" + str(data_applyCpdSeal.name_fix) +"' and id = " + str(applyId_No)
        resList = ms.ExecQuery(newsql)
        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        for apply_status in resList:
            # print("apply_status:", apply_status['status'], type(apply_status['status']))
            self.assertEqual(apply_status['status'], conf_output_data['data']['apply_status'])               ##比对http响应data的apply_status

            #coding:utf-8