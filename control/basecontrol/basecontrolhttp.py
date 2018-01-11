#coding:utf-8
'''
title:控制模块   control
author:Robert
date:20171115
email:luoshuibo@vcredut.com
'''
from configparser import ConfigParser

class controlActionsHttp():
    '''
        ControlActions类
    '''

    def get_prefix_url(confname,section):
        '''
        生成http形式的请求前缀url ,比如http://10.139.60.158:8080/
        :param sectionname:
        :param keyname:
        :return:
        '''
        cfg = ConfigParser()
        conf = cfg.read(confname)
        temp_prefix_url = cfg.get(section, 'hostname') + ':' + cfg.get(section, 'port')
        prefix_url = 'http://' + str(temp_prefix_url)
        # print('prefix_url',prefix_url)
        return prefix_url

    def get_request_header(confname):
        '''
        生成http形式的请求url ,比如http://10.139.60.158:8080/
        :param sectionname:
        :param keyname:
        :return:
        '''
        cfg = ConfigParser()
        conf = cfg.read(confname)
        temp_prefix_url = cfg.get('serverconfig', 'hostname') + ':' + cfg.get('serverconfig', 'port')
        prefix_url = 'http://' + str(temp_prefix_url)
        return prefix_url

