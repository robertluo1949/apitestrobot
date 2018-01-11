#coding:utf-8
'''
title:控制模块   control ini配置文件的读写
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
from configparser import ConfigParser

class controlActionsIni():
    '''
        ControlActions类
    '''
    def get_ini_value(confname,sectionname,keyname):
        '''
        该函数可以获取配置文件confname的某区域sectionname某一个键keyname的值
        :param confname:
        :param sectionname:
        :param keyname:
        :return:
        '''
        cfg=ConfigParser()
        conf=cfg.read(confname)
        temp_s = cfg.sections()
        temp_fp = cfg.options(sectionname)
        r_value = cfg.get(sectionname, keyname)
        return r_value

    def get_report_name(confname):
        '''
        生成http形式的请求url ,比如http://10.139.60.158:8080/
        :param sectionname:
        :param keyname:
        :return:
        '''
        cfg=ConfigParser()
        conf = cfg.read(confname)
        temp_prefix_url=cfg.get('serverconfig','hostname')+':'+cfg.get('serverconfig','port')
        prefix_url='http://'+str(temp_prefix_url)
        return prefix_url

