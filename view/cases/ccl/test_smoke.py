# coding:utf-8
'''
title:测试用例关于API的测试用例
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
import json
import sys
import unittest

import requests
from view.datas.ccl import data_smoke
from control.basecontrol import basecontrolini
from control.basecontrol import basecontrolhttp


class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_applogin(self):
        print('path',sys.path[0])
        # prefix_url = basecontrolini.ControlActions.get_prefix_url(sys.path[0] + '\\conf.ini')
        prefix_url = basecontrolhttp.controlActionsHttp.get_prefix_url(sys.path[0] + '\\conf.ini','serverbeta5')
        print('path',sys.path[0])
        url = prefix_url + '/ccl/data/ws/rest/app/login'

        t_data =data_smoke.input_data    ##引入测试需要的输入参数view.datas.ccl
        print('t_data',t_data)
        output_content =data_smoke.output_data

        t_headers = {'Content-Type': 'application/json'}
        t_request = requests.post(url, data=json.dumps(t_data), headers=t_headers)

        self.assertEqual(t_request.status_code, 200)

    def test_Case2(self):
        self.assertEqual(2, 2, "testError")
        #coding:utf-8