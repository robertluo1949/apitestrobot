# coding:utf-8
'''
title:测试用例关于API的测试用例
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
import unittest


class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_applogin(self):
        self.assertEqual(200, 200)

    def test_Case2(self):
        self.assertEqual(2, 2, "testError")
        #coding:utf-8