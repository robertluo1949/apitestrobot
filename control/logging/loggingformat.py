#coding:utf-8
'''
title:打印日志功能
author:Robert
date:20171127
email:luoshuibo@vcredut.com
content:
other:
'''
# 第一步，创建一个logger
import logging
import sys
from _datetime import datetime
from control.basecontrol.basecontrolini import controlActionsIni


class logsetting(logging) :
    def setlogfile(self,currpath,confname):
        '''
        :param currpath
        :param confname
        :return: filePath
        '''
        postfix = datetime.now().strftime('%Y%m%d_%H%M%S')
        currpath = sys.path[0]  ##获取工作路径
        conffile = 'conf.ini'  ##
        print('currpath', currpath)
        value_path = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'logs', 'path')
        value_prefix = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'logs',
                                                       'reportprefix')
        # print('value_path', value_path)
        # print('value_prefix', value_prefix)
        # filePath =value_path+value_prefix+str(postfix)+'.html'   ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        filePath = value_path + str(value_prefix) + str(
            postfix) + '.html'  ##生成报告的路径value_path和文件名字value_prefix+postfix+'.html'
        print('filePath', filePath)
        return filePath

    def setloglevel(self):
        logger = self.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关
        return logger

    def setloghander(self,logfile):


        # 第二步，创建一个handler，用于写入日志文件
        # logfile = 'd:\\logs\\log.log'
        # postfix = datetime.now().strftime('%Y%m%d_%H%M%S')
        currpath = sys.path[0]  ##获取工作路径
        conffile = 'conf.ini'  ##
        #
        logfile = controlActionsIni.get_ini_value(currpath + '\\' + conffile, 'logs', 'path')
        print('logfile',logfile)

        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)

# # 日志
# logger.debug('this is a logger debug message')
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')