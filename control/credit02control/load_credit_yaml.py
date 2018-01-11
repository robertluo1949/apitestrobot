#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import sys

#read config.yaml 返回filesystempath的路径名
class LoadFileSystempath:
    paramValue=''
    def getValue(self,params):
        f=open(sys.path[0].join('\/view\/datas\/credit02\/').join('credit_config.yaml'))
        x=yaml.load(f)
        print (x)
        paramValue= x[params]
        f.close()
        #print paramValue
        return paramValue

           
#lc= LoadFileSystempath()
#lc.getValue('fileSystempath');