#coding:utf-8
'''
title:逻辑控制模块   control
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
import os,sys
from view.cases.pay import test_on2 as payteston
from view.cases.contract import test_on1 as contractteston
from view.cases.seal import test_applyCpdSeal as test_applyCpdSeal
from view.cases.seal import test_getCpdSeal as test_getCpdSeal
from view.cases.seal import test_queryCpdSeal as test_queryCpdSeal
from view.cases.credit01 import test_fengniao as test_fengniao
from view.cases.credit01 import test_getZyCrInfo as test_getZyCrInfo
from view.cases.credit01 import test_reportInfo as test_reportInfo
from view.cases.credit01 import test_getBsCrInfo as test_getBsCrInfo
from view.cases.credit02 import test_applyCrRp_ZY as test_applyCrRp_ZY
from view.cases.credit02 import test_getCrRp_ZY as test_getCrRp_ZY
from view.cases.credit02 import test_applyCrRp_ZH as test_applyCrRp_ZH
from view.cases.credit02 import test_getCrRp_ZH as test_getCrRp_ZH
from view.cases.cfca import test_applyMultiple as test_applyMultiple
from view.cases.cfca import test_applyOne as test_applyOne
import view.cases.contract.test_on1 as contracton
import unittest

class modelMicroserver(unittest.TestSuite):
    '''
    组织每个单元测试成一个模型。
    微服务的测试模型包括：支付pay，签章seal，合同contract
    '''
    def SuiteMulti(self):
        '''
        :
        :return: suitTest
        '''
        # suitepay=payteston.payTest()
        # print('pay', suitepay)
        # ##加载支付的测试脚本
        # suitecontract=contractteston.contractTest()                ##加载支付的测试脚本
        # print('suitecontract',suitecontract)
        # suitTest=unittest.TestSuite((suitepay,suitecontract))  ##把多个脚本合并到一个测试套件testsuite

        suitTest = unittest.TestSuite()
        # suitTest.addTests(unittest.makeSuite(contractteston.contractTest))  ####加载合同的testcase
        # suitTest.addTests(unittest.makeSuite(payteston.payTest))            ####加载支付的testcase
        # suitTest.addTests(unittest.makeSuite(sealteston.sealTest))          ####加载签章的testcase
        suitTest.addTests(unittest.makeSuite(test_fengniao.queryZyxfjrCreditInfoCase))       ####加载征信一期的queryZyxfjrCreditInfo接口
        suitTest.addTests(unittest.makeSuite(test_getZyCrInfo.GetZyxfjrCreditInfo))          ####加载征信一期的GetZyxfjrCreditInfo接口
        suitTest.addTests(unittest.makeSuite(test_reportInfo.ReportInfo))                    ####加载征信一期的ReportInfo接口
        suitTest.addTests(unittest.makeSuite(test_getBsCrInfo.GetBaoShangCreditInfo))        ####加载征信一期的GetBaoShangCreditInfo接口
        suitTest.addTests(unittest.makeSuite(test_applyCrRp_ZY.applyCreditReport_ZY))        ####加载征信二期的applyCreditReport接口(中原)
        suitTest.addTests(unittest.makeSuite(test_getCrRp_ZY.getCreditReport_ZY))            ####加载征信二期的getCreditReport接口(中原)
        suitTest.addTests(unittest.makeSuite(test_applyCrRp_ZH.applyCreditReport_ZH))        ####加载征信二期的applyCreditReport接口(中航)
        suitTest.addTests(unittest.makeSuite(test_getCrRp_ZH.getCreditReport_ZH))            ####加载征信二期的getCreditReport接口(中航)
        # suitTest.addTests(unittest.makeSuite(test_applyCpdSeal.applyCompoundSeal))           ####加载签章一期的applyCompoundSeal接口
        # suitTest.addTests(unittest.makeSuite(test_getCpdSeal.getCompoundSeal))               ####加载签章一期的getCompoundSeal接口
        # suitTest.addTests(unittest.makeSuite(test_queryCpdSeal.queryCompoundSeal))           ####加载签章一期的queryCompoundSeal接口
        suitTest.addTests(unittest.makeSuite(test_applyMultiple.applyMultiple))               ####加载签章二期的applyMultiple接口
        suitTest.addTests(unittest.makeSuite(test_applyOne.applyOne))                         ####加载签章二期的applyOne接口


        return suitTest

    def SuiteMap(self):
        '''
        :return: suitTest
        '''
        testspay = ['test_Case1', 'test_Case2']
        testscontract = ['test_Case3', 'test_Case4']
        return unittest.TestSuite(map(contracton.contractTest,testscontract))
