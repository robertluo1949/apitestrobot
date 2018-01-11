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

    #确定生成报告的路径  确定html报告中的title,description,author
    filePath =controlActionsReport.get_report_name(sys.path[0],'conf.ini')
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