#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

##签章一期接口的请求database定义
host = '10.139.60.143'
user = 'u_panzongwei'
pwd = 'Vcredit1@3'
db = 'kkdseal'

##签章一期接口的请求路径定义
ad_getCompoundSeal = '/micro/seal/getCompoundSeal'

##重复申请使用的名字和身份证
name_fix = "小十聪"
identityNo_fix = "430521199207220482"
applyId_fix = "28"

#CaseNo10411
#验证使用合法的account、password、certNo、name和applyId，取得授权书正常
#getCompoundSeal接口所需要提供的输入数据  data input
getCompoundSealInput01 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":str(identityNo_fix),
                          "name": str(name_fix),
                          "applyId": str(applyId_fix)}

##getCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
getCompoundSealOutput01 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": None,
        "optInfo": "success",
        "dfsPathList": ['group1/M00/2F/40/Cos8o1odU0WAD_N1AAVIF3zTdlY353.pdf'],
        "coaBase64List": not None
    }
}


#CaseNo10412
#验证不指定applyId时，取得授权书异常
#getCompoundSeal接口所需要提供的输入数据  data input
getCompoundSealInput02 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":str(identityNo_fix),
                          "name": str(name_fix),
                          "applyId": ""}

##getCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
getCompoundSealOutput02 ={
    "status": "1",
    "msg": "fail",
    "data": {
        "optResult": None,
        "optInfo": "fail",
        "dfsPathList": [],
        "coaBase64List": []
    }
}

#CaseNo10413
#验证输入不存在的applyId时，申请授权书异常
#getCompoundSeal接口所需要提供的输入数据  data input
getCompoundSealInput03 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":str(identityNo_fix),
                          "name": str(name_fix),
                          "applyId": "999999999"}

##getCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
getCompoundSealOutput03 ={
    "status": "1",
    "msg": "fail",
    "data": {
        "optResult": None,
        "optInfo": "fail",
        "dfsPathList": [],
        "coaBase64List": []
    }
}
