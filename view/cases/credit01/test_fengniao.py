# coding:utf-8
'''
title:测试去蜂鸟查征信报告用例
author:Shiyunliang
date:20171128
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.credit01 import  data_fengniao

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'microserverbeta4')
url = prefix_url + data_fengniao.ad_fengniao
t_headers = {'Content-Type': 'application/json'}

class queryZyxfjrCreditInfoCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_No10101 (self):
        """征信一期：验证使用合法的身份证号，报告编号和报告ID为空，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input01                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output01                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10102 (self):
        """征信一期：验证使用合法的身份证号，报告编号为空，报告ID不为空，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input02                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output02                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10103 (self):
        """征信一期：验证使用合法的身份证号，报告编号不为空，报告ID为空，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input03                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output03                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10104 (self):
        """征信一期：验证使用合法的身份证号，报告编号和报告ID不为空，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input04                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output04                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10105 (self):
        """征信一期：验证不指定平台账号，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input05                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output05                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10106 (self):
        """征信一期：验证不指定平台密码，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input06                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output06                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10107 (self):
        """征信一期：验证输入无效的平台账号，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input07                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output07                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10108 (self):
        """征信一期：验证输入无效的平台密码，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input08                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output08                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10109 (self):
        """征信一期：验证不指定身份证号码，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input09                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output09                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10110 (self):
        """征信一期：验证输入无效的身份证号码，申请蜂鸟征信异常"""
        conf_input_data = data_fengniao.input10                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output10                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10111 (self):
        """征信一期：验证使用合法的身份证号，客户姓名为空，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input11                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output11                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData

    def test_No10112 (self):
        """征信一期：验证使用合法的身份证号，无效的客户姓名，申请蜂鸟征信正常"""
        conf_input_data = data_fengniao.input12                                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_fengniao.output12                                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##请求蜂鸟查征信报告
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['reportNo'],conf_output_data['data']['reportNo'])            ##比对http响应data的reportNo
        self.assertEqual(re_output_data['data']['reportData'], conf_output_data['data']['reportData'])      ##比对http响应data的reportData


            #coding:utf-8