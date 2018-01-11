# coding:utf-8
'''
title:测试获取用户在蜂鸟的信用报告给包商用例
author:Shiyunliang
date:20171129
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.credit01 import  data_getBsCrInfo

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta4')
url = prefix_url + data_getBsCrInfo.ad_getBsCrInfo
t_headers = {'Content-Type': 'application/json'}

class GetBaoShangCreditInfo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_No10123 (self):
        """征信一期：验证使用合法的信用报告编号，获取征信报告给包商正常"""
        conf_input_data = data_getBsCrInfo.input01                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output01                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10124 (self):
        """征信一期：验证不指定平台账号，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input02                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output02                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10125 (self):
        """征信一期：验证不指定平台密码，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input03                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output03                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10126 (self):
        """征信一期：验证不指定信用报告编号，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input04                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output04                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10127 (self):
        """征信一期：验证输入无效的平台账号，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input05                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output05                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10128 (self):
        """征信一期：验证输入无效的平台密码，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input06                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output06                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

    def test_No10129 (self):
        """征信一期：验证输入无效的信用报告编号，获取征信报告给包商异常"""
        conf_input_data = data_getBsCrInfo.input07                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getBsCrInfo.output07                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        if re_output_data['data']['reportData'] == None:
            self.assertEqual(re_output_data['data']['reportNo'], conf_output_data['data']['reportNo'])      ##比对http响应data的reportNo
        else :
            self.assertEqual(re_output_data['data']['reportData']['reportNo'], conf_output_data['data']['reportData']['reportNo'])      ##比对http响应data的reportData的reportNo

            #coding:utf-8