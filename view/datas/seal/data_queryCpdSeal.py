#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

##签章一期接口的请求database定义
host = '10.139.60.143'
user = 'u_panzongwei'
pwd = 'Vcredit1@3'
db = 'kkdseal'

##签章一期接口的请求路径定义
ad_queryCompoundSeal = '/micro/seal/queryCompoundSeal'

##重复申请使用的名字和身份证
name_fix = "小十聪"
identityNo_fix = "430521199207220482"
applyId_fix = "28"
identityNo_err = "111111111111111111"

#CaseNo10421
#验证使用合法的account、password、certNo和name，取得授权书ID正常
#queryCompoundSeal接口所需要提供的输入数据  data input
queryCompoundSealInput01 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":str(identityNo_fix),
                          "name": str(name_fix)}

##queryCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
queryCompoundSealOutput01 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": None,
        "optInfo": "success",
        "applyId": applyId_fix
    }
}


#CaseNo10422
#验证不指定certNo时，取得授权书ID异常
#queryCompoundSeal接口所需要提供的输入数据  data input
queryCompoundSealInput02 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":"",
                          "name": str(name_fix)}

##queryCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
queryCompoundSealOutput02 ={
    "status": "1",
    "msg": "该身份证号不存在授权书",
    "data": {
        "optResult": None,
        "optInfo": "noExist",
        "applyId": None
    }
}

#CaseNo10423
#验证输入不存在的certNo时，申请授权书ID异常
#queryCompoundSeal接口所需要提供的输入数据  data input
queryCompoundSealInput03 = {"account":"kkfund",
                          "password":"laPAP4OMjbnIdXA8hvqWpQ==",
                          "certNo":str(identityNo_err),
                          "name": str(name_fix)}

##queryCompoundSeal接口所需要提供的输出数据  ,方便进行比对  data output
queryCompoundSealOutput03 ={
    "status": "1",
    "msg": "该身份证号" + str(identityNo_err) + "不存在授权书",
    "data": {
        "optResult": None,
        "optInfo": "noExist",
        "applyId": None
    }
}
