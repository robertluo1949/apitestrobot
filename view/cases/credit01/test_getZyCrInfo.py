# coding:utf-8
'''
title:测试获取用户在蜂鸟的信用报告给中原消费金融用例
author:Shiyunliang
date:20171129
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.credit01 import  data_getZyCrInfo

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta4')
url = prefix_url + data_getZyCrInfo.ad_getZyCrInfo
t_headers = {'Content-Type': 'application/json'}

class GetZyxfjrCreditInfo(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_No10113 (self):
        """征信一期：验证使用合法的信用报告编号，获取征信报告给中原消金正常"""
        conf_input_data = data_getZyCrInfo.input01                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output01                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10114 (self):
        """征信一期：验证不指定平台账号，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input02                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output02                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10115 (self):
        """征信一期：验证不指定平台密码，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input03                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output03                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10116 (self):
        """征信一期：验证不指定信用报告编号，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input04                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output04                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10117 (self):
        """征信一期：验证输入无效的平台账号，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input05                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output05                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10118 (self):
        """征信一期：验证输入无效的平台密码，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input06                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output06                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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

    def test_No10119 (self):
        """征信一期：验证输入无效的信用报告编号，获取征信报告给中原消金异常"""
        conf_input_data = data_getZyCrInfo.input07                                                              ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getZyCrInfo.output07                                                            ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

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