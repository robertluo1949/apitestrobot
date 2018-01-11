#coding:utf-8
'''
title:控制模块   control 报告的读写
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
import sys
from datetime import datetime

from control.basecontrol.basecontrolini import controlActionsIni


class controlActionsReport():
    '''
        ControlActions类
    '''
    def get_report_name(currpath,confname):
        '''
        :param currpath
        :param confname
        :return: filePath
        '''
        postfix = datetime.now().strftime('%Y%m%d_%H%M%S')
        currpath = sys.path[0]  ##获取工作路径
        conffile = 'conf.ini'  ##
        print('currpath', currpath)
        value_path = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'reports', 'path')
        value_prefix = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'reports',
                                                                      'reportprefix')
        # print('value_path', value_path)
        # print('value_prefix', value_prefix)
        # filePath =value_path+value_prefix+str(postfix)+'.html'   ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        filePath = value_path + str(value_prefix) + str(
            postfix) + '.html'  ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        print('filePath', filePath)
        return  filePath

    def get_report_name_buildid(currpath,confname,buildid):
        '''
        :desc   针对Jenkins衔接，生成测试报告名字,报告中参数
        :param currpath
        :param confname
        :param buildid  来源于jenkins的运行变量BUILD_ID
        :return: filePath
        '''
        postfix = buildid   ##获取buildid
        currpath = sys.path[0]  ##获取工作路径
        conffile = 'conf.ini'  ##
        print('currpath', currpath)
        value_path =controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'reports',
                                                                      'jenkins_temppath')
        value_prefix = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'reports',
                                                                      'reportprefix')
        # print('value_path', value_path)
        # print('value_prefix', value_prefix)
        # filePath =value_path+value_prefix+str(postfix)+'.html'   ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        filePath = value_path + str(value_prefix) + str(
            postfix) + '.html'  ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        print('filePath', filePath)
        return  filePath

    def get_report_atribute(currpath,confname,item):
        '''
        :param currpath
        :param confname
        :return: filePath
        '''
        value_item = controlActionsIni.get_ini_value(currpath + '\\' + confname, 'reports',item)
        return  value_item