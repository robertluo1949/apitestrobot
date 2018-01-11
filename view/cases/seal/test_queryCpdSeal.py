# coding:utf-8
'''
title:测试取得授权书ID用例
author:Shiyunliang
date:20171211
email:shiyunliang@vcredut.com
'''
import json
import sys
import unittest
import time

import requests
from view.datas.seal import data_queryCpdSeal

from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp
from control.basecontrol import basemssql

prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini', 'serverbeta5_seal')
url = prefix_url + data_queryCpdSeal.ad_queryCompoundSeal
t_headers = {'Content-Type': 'application/json'}
ms = basemssql.mssqlaction(host=data_queryCpdSeal.host, user=data_queryCpdSeal.user, pwd=data_queryCpdSeal.pwd, db=data_queryCpdSeal.db)


class queryCompoundSeal(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ##清除签章产生的数据

        pass

    def test_No10421 (self):
        """签章一期：验证使用合法的输入参数，取得授权书ID正常"""

        conf_input_data = data_queryCpdSeal.queryCompoundSealInput01                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_queryCpdSeal.queryCompoundSealOutput01                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        #避免过于频繁的连接数据库
        time.sleep(1)

        certNo = conf_input_data['certNo']

        newsql = "select id from [dbo].[t_cr_coa_apply] WHERE identity_no = '" + str(certNo) +"' and status = '1'"
        resList = ms.ExecQuery(newsql)

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        ##验证返回的applyId和DB项目是否匹配
        for apply_id in resList:
            # print("apply_status:", apply_id['id'], type(apply_id['id']))
            self.assertEqual(re_output_data['data']['applyId'], apply_id['id'])                               ##比对http响应data的applyId

    def test_No10422(self):
        """签章一期：不输入身份证号码，取得授权书ID异常"""

        conf_input_data = data_queryCpdSeal.queryCompoundSealInput02                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_queryCpdSeal.queryCompoundSealOutput02                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['applyId'], conf_output_data['data']['applyId'])             ##比对http响应data的applyId


    def test_No10423(self):
        """签章一期：输入不存在的身份证号码，取得授权书ID异常"""

        conf_input_data = data_queryCpdSeal.queryCompoundSealInput03                                           ##conf_input_data  賦值获取输入测试的输入参数，已经预先配置好
        conf_output_data = data_queryCpdSeal.queryCompoundSealOutput03                                         ##conf_output_content  賦值获取输入测试的输出参数，已经预先配置好

        request_content = requests.post(url, data=json.dumps(conf_input_data), headers=t_headers)               ##申请复合签章
        re_output_data= request_content.json()                                                                  ##把http请求的响应内容进行json格式化

        self.assertEqual(re_output_data['status'],conf_output_data['status'])                                 ##比对http响应status
        self.assertEqual(re_output_data['msg'], conf_output_data['msg'])                                       ##比对http响应msg
        self.assertEqual(re_output_data['data']['optResult'],conf_output_data['data']['optResult'])         ##比对http响应data的optResult
        self.assertEqual(re_output_data['data']['optInfo'], conf_output_data['data']['optInfo'])             ##比对http响应data的optInfo
        self.assertEqual(re_output_data['data']['applyId'], conf_output_data['data']['applyId'])             ##比对http响应data的applyId

            #coding:utf-8