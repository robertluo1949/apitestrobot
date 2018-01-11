#coding:utf-8

##接口的请求路径定义
ad_getZyCrInfo = '/micro/credit/GetZyxfjrCreditInfo'

##case01:
##验证使用合法的account、password和reportNo为空，获取征信正常
input01 = {
    "account": "kkfund",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "reportNo": "100000000210"
}
##征信内容获取正常
output01 ={
    "status": "0",
    "msg": "查询征信数据成功",
    "data": {
        "optResult": "0",
        "optInfo": "查询征信数据成功",
        "reportNo": None,
        "reportData": {
            "reportNo": "100000000210"
        }
    }
}

##case02:
##验证不指定account时，获取征信异常
input02 = {
    "account": "",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "reportNo": "100000000210"
}
##不输入平台账号，获取内容为空
output02 ={
    "status": "1",
    "msg": "平台账号、平台密码、信用报告编号均不能为空",
    "data": {
        "optResult": "1",
        "optInfo": "平台账号、平台密码、信用报告编号均不能为空",
        "reportNo": None,
        "reportData": None
    }
}

##case03:
##验证不指定password时，获取征信异常
input03 = {
    "account": "fengniao",
    "password": "",
    "reportNo": "100000000210"
}
##不输入平台密码，获取内容为空
output03 ={
    "status": "1",
    "msg": "平台账号、平台密码、信用报告编号均不能为空",
    "data": {
        "optResult": "1",
        "optInfo": "平台账号、平台密码、信用报告编号均不能为空",
        "reportNo": None,
        "reportData": None
    }
}

##case04:
##验证不指定reportNo时，获取征信异常
input04 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "reportNo": ""
}
##不输入信用报告编号，获取内容为空
output04 ={
    "status": "1",
    "msg": "平台账号、平台密码、信用报告编号均不能为空",
    "data": {
        "optResult": "1",
        "optInfo": "平台账号、平台密码、信用报告编号均不能为空",
        "reportNo": None,
        "reportData": None
    }
}

##case05:
##验证输入无效的account时，获取征信异常
input05 = {
    "account": "123456789",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "reportNo": "100000000210"
}
##输入无效的平台账号，获取内容为空
output05 ={
    "status": "1",
    "msg": "该用户不存在",
    "data": {
        "optResult": "1",
        "optInfo": "该用户不存在",
        "reportNo": None,
        "reportData": None
    }
}

##case06:
##验证输入无效的password时，获取征信异常
input06 = {
    "account": "fengniao",
    "password": "123456789",
    "reportNo": "100000000210"
}
##输入无效的平台密码，获取内容为空
output06 ={
    "status": "1",
    "msg": "该用户不存在",
    "data": {
        "optResult": "1",
        "optInfo": "该用户不存在",
        "reportNo": None,
        "reportData": None
    }
}

##case07:
##验证输入无效的reportNo时，获取征信异常
input07 = {
    "account": "fengniao",
    "password": "laPAP4OMjbnIdXA8hvqWpQ==",
    "reportNo": "999999999999"
}
##输入无效的信用报告编号，获取内容为空
output07 ={
    "status": "1",
    "msg": "账号、密码、信用报告编号错误或者客户征信数据不存在",
    "data": {
        "optResult": "1",
        "optInfo": "账号、密码、信用报告编号错误或者客户征信数据不存在",
        "reportNo": None,
        "reportData": None
    }
}