#coding:utf-8
'''
title:逻辑控制模块   control
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
import unittest
import os,sys
from view.cases.ccl import test_smoke,test_regression



def SuiteDiscover(casespath):
    '''
    :param casespath   ##装在测试用例的路径
    :return: suiteTest
    '''
    #定义一个单元测试容器
    ##
    # suiteTest = unittest.defaultTestLoader.discover("C:\\Users\\luoshuibo\\PycharmProjects\\autotest\\view\\ccl", pattern='*test*',top_level_dir = None)
    #将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
    suiteTest = unittest.defaultTestLoader.discover(casespath, pattern='test_*',top_level_dir = None)
    print(suiteTest)
    return suiteTest


