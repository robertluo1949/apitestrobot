#coding:utf-8

##接口的请求路径定义
ad_fengniao = '/micro/credit/queryZyxfjrCreditInfo'

##case01:
##验证使用合法的account、password、identityNo和name，reportSn和reportID为空，获取征信正常
input01 = {
    "account": "kkfund",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "530322199005292217",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##征信内容获取正常
output01 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000210",
        "reportData": {
            "reportId": 209,
            "reportSn": "2017062900004139875112",
            "reportCreateTime": "2017-06-29T16:06:34",
            "sourceType": "11"
        }
    }
}

##case02:
##验证使用合法的account、password、identityNo和name，reportSn=空和reportID<>空，获取征信正常
input02 = {
    "account": "kkfund",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "",
    "name": "小白",
    "reportSn": "",
    "reportId": "209"
}
##征信过期两个月，获取内容为空
output02 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000210",
        "reportData": None
    }
}

##case03:
##验证使用合法的account、password、identityNo和name，reportSn<>空和reportID=空，获取征信正常
input03 = {
    "account": "kkfund",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "",
    "name": "小白",
    "reportSn": "2017062900004139875112",
    "reportId": ""
}
##征信过期两个月，获取内容为空
output03 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000210",
        "reportData": None
    }
}

##case04:
##验证使用合法的account、password、identityNo和name，reportSn和reportID<>空，获取征信正常
input04 = {
    "account": "kkfund",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "",
    "name": "小白",
    "reportSn": "2017062900004139875112",
    "reportId": "209"
}
##征信过期两个月，获取内容为空
output04 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000210",
        "reportData": None
    }
}

##case05:
##验证不指定account时，获取征信异常
input05 = {
    "account": "",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "530322199005292217",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##不输入平台账号，获取内容为空
output05 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "1",
        "optInfo": "平台账号、平台密码均不能为空",
        "reportNo": None,
        "reportData": None
    }
}

##case06:
##验证不指定password时，获取征信异常
input06 = {
    "account": "kkfund",
    "password": "",
    "identityNo": "530322199005292217",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##不输入平台密码，获取内容为空
output06 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "1",
        "optInfo": "平台账号、平台密码均不能为空",
        "reportNo": None,
        "reportData": None
    }
}

##case07:
##验证输入无效的account时，获取征信异常
input07 = {
    "account": "1234567890ABCDEFG",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "530322199005292217",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##输入无效的平台账号，获取内容为空
output07 ={
    "status": "1",
    "msg": "该用户不存在",
    "data": {
        "optResult": "1",
        "optInfo": "该用户不存在",
        "reportNo": None,
        "reportData": None
    }
}

##case08:
##验证输入无效的secret时，获取征信异常
input08 = {
    "account": "kkfund",
    "password": "1234567890ABCDEFG",
    "identityNo": "530322199005292217",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##输入无效的密码，获取内容为空
output08 ={
    "status": "1",
    "msg": "该用户不存在",
    "data": {
        "optResult": "1",
        "optInfo": "该用户不存在",
        "reportNo": None,
        "reportData": None
    }
}

##case09:
##验证不指定identityNo时，获取征信异常
input09 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##不输入身份证号码，获取内容为空
output09 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "1",
        "optInfo": "报告编号、报告id和身份证号不可都为空",
        "reportNo": None,
        "reportData": None
    }
}

##case10:
##验证输入无效的identityNo时，获取征信异常
input10 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "1234567890ABCDEFG",
    "name": "小白",
    "reportSn": "",
    "reportId": ""
}
##输入无效的身份证号码，获取内容为空
output10 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "1",
        "optInfo": "身份证号:1234567890ABCDEFG在蜂鸟无报告",
        "reportNo": None,
        "reportData": None
    }
}

##case11:
##验证不指定name时，获取征信正常
input11 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "310101198909231064",
    "name": "",
    "reportSn": "",
    "reportId": ""
}
##不输入客户姓名，获取内容正常
output11 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000219",
        "reportData": {
            "reportId": 317,
            "reportSn": "2017092100004485348240",
            "reportCreateTime": "2017-09-21T12:19:09",
            "sourceType": "13"
        }
    }
}

##case12:
##验证输入无效的name时，获取征信正常
input12 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "identityNo": "341225199106270016",
    "name": "123456789",
    "reportSn": "",
    "reportId": ""
}
##输入无效的客户姓名，获取内容 正常
output12 ={
    "status": "0",
    "msg": "success",
    "data": {
        "optResult": "0",
        "optInfo": "success",
        "reportNo": "100000000218",
        "reportData": {
            "reportId": 240,
            "reportSn": "2017080200004280007638",
            "reportCreateTime": "2017-08-02T09:58:16",
            "sourceType": "11"
        }
    }
}