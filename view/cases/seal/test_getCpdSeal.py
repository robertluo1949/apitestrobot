# coding:utf-8
'''
title:测试取得授权书用例
author:Shiyunliang
date:20171211
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.seal import data_getCpdSeal

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'serverbeta5_seal')
url = prefix_url + data_getCpdSeal.ad_getCompoundSeal
t_headers = {'Content-Type': 'application/json'}


class getCompoundSeal(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ##清除签章产生的数据

        pass

    def test_No10411 (self):
        """签章一期：验证使用合法的输入参数，取得授权书正常"""

        conf_input_data = data_getCpdSeal.getCompoundSealInput01                                                 ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getCpdSeal.getCompoundSealOutput01                                               ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##取得授权书
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['dfsPathList'], conf_output_data['data']['dfsPathList'])    ##比对http响应data的dfsPathList
        if re_output_data['data']['coaBase64List'] != None :
            self.assertEqual(1, 1, "coaBase64List is None")                                                   ##比对http响应data的coaBase64List
        else :
            self.assertEqual(0, 1, "coaBase64List is None")                                                   ##比对http响应data的coaBase64List

    def test_No10412(self):
        """签章一期：不指定申请授权书ID，取得授权书异常"""

        conf_input_data = data_getCpdSeal.getCompoundSealInput02                                                  ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getCpdSeal.getCompoundSealOutput02                                                ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##取得授权书
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['dfsPathList'], conf_output_data['data']['dfsPathList'])    ##比对http响应data的dfsPathList
        self.assertEqual(re_output_data['data']['coaBase64List'], conf_output_data['data']['coaBase64List'])  ##比对http响应data的coaBase64List

    def test_No10413(self):
        """签章一期：输入不存在的申请授权书ID，申请授权书异常"""

        conf_input_data = data_getCpdSeal.getCompoundSealInput03                                                ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_getCpdSeal.getCompoundSealOutput03                                              ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##取得授权书
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['dfsPathList'], conf_output_data['data']['dfsPathList'])    ##比对http响应data的dfsPathList
        self.assertEqual(re_output_data['data']['coaBase64List'], conf_output_data['data']['coaBase64List'])  ##比对http响应data的coaBase64List

            #coding:utf-8