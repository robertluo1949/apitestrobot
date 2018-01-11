# coding:utf-8
'''
title:测试获取用户从渠道(中航)征信报告用例
author:Shiyunliang
date:20171129
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.credit02 import data_credit02_ZH

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta7')
url = prefix_url + data_credit02_ZH.ad_getCreditReport_ZH
t_headers = {'Content-Type': 'application/json'}

class getCreditReport_ZH(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_No10271 (self):
        """征信二期：验证使用合法的信用报告编号，获取中航征信报告正常"""
        conf_input_data = data_credit02_ZH.getCreditInput01                                                          ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput01                                                        ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10272 (self):
        """征信二期：不指定渠道代码，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput02                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput02                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10273(self):
        """征信二期：不指定平台账号，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput03                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput03                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10274(self):
        """征信二期：不指定平台密码，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput04                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput04                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10275(self):
        """征信二期：不指定信用报告编号，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput05                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput05                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10276(self):
        """征信二期：输入无效的渠道代码，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput06                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput06                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10277(self):
        """征信二期：输入无效的平台账号，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput07                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput07                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10278(self):
        """征信二期：输入无效的平台密码，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput08                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput08                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10279(self):
        """征信二期：输入无效的信用报告编号，获取中航征信报告异常"""
        conf_input_data = data_credit02_ZH.getCreditInput09                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput09                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10280(self):
        """征信二期：输入长度超长的信用报告编号，系统异常"""
        conf_input_data = data_credit02_ZH.getCreditInput10                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZH.getCreditOutput10                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中航)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

            #coding:utf-8