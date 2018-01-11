# -*- coding:utf-8 -*-
'''
titile : start to testing with discover method
author:Robert
date:20171117
version:python3.6
'''

import sys

import model.microserver  as modelmicroserver
from control.basecontrol.basecontrolreport import controlActionsReport
from control.lib.htmlreport.HTMLTestReportEN import HTMLTestRunner

if __name__ == '__main__':

    filePath = controlActionsReport.get_report_name_buildid(sys.path[0], 'conf.ini', sys.argv[1])
    print('报告标号 jenkins 传送 sys.argv[1]',sys.argv[1])
    re_title =controlActionsReport.get_report_atribute(sys.path[0],'conf.ini','title')
    re_description =controlActionsReport.get_report_atribute(sys.path[0],'conf.ini','description')
    re_author =controlActionsReport.get_report_atribute(sys.path[0],'conf.ini','author')
    # fp = open(filePath,mode="wb")

    with open(filePath,mode="wb") as fp:
    #生成报告的Title,描述
        runner =  HTMLTestRunner(
            stream=fp,
            title=re_title,
            description=re_description,
            tester=re_author
            )
        #运行测试用例
        modolm=modelmicroserver.modelMicroserver()
        testsuite=modolm.SuiteMulti()
        runner.run(testsuite)
        # 关闭文件，否则会无法生成文件
        fp.close()