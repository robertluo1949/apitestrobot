# coding:utf-8
'''
title:测试获取用户从渠道(中原)征信报告用例
author:Shiyunliang
date:20171129
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.credit02 import data_credit02_ZY

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta7')
url = prefix_url + data_credit02_ZY.ad_getCreditReport_ZY
t_headers = {'Content-Type': 'application/json'}

class getCreditReport_ZY(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_No10251 (self):
        """征信二期：验证使用合法的信用报告编号，获取中原征信报告正常"""
        conf_input_data = data_credit02_ZY.getCreditInput01                                                          ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput01                                                        ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10252 (self):
        """征信二期：不指定渠道代码，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput02                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput02                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10253(self):
        """征信二期：不指定平台账号，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput03                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput03                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10254(self):
        """征信二期：不指定平台密码，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput04                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput04                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10255(self):
        """征信二期：不指定信用报告编号，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput05                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput05                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10256(self):
        """征信二期：输入无效的渠道代码，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput06                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput06                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10257(self):
        """征信二期：输入无效的平台账号，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput07                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput07                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10258(self):
        """征信二期：输入无效的平台密码，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput08                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput08                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10259(self):
        """征信二期：输入无效的信用报告编号，获取中原征信报告异常"""
        conf_input_data = data_credit02_ZY.getCreditInput09                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput09                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

    def test_No10260(self):
        """征信二期：输入长度超长的信用报告编号，系统异常"""
        conf_input_data = data_credit02_ZY.getCreditInput10                                                        ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_credit02_ZY.getCreditOutput10                                                      ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请渠道(中原)征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] != None:
            self.assertEqual(re_output_data['data']['reportData']['reportNo'],conf_output_data['data']['reportData']['reportNo'])            ##比对http响应data的reportData的reportNo
            self.assertEqual(re_output_data['data']['reportData']['fnReportId'],conf_output_data['data']['reportData']['fnReportId'])  ##比对http响应data的reportData的fnReportId

            #coding:utf-8