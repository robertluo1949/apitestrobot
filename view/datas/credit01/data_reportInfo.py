#coding:utf-8

##接口的请求路径定义
ad_reportInfo = '/micro/credit/OrgCredit/Query/ReportInfo'

##case01:
##验证使用合法的certNo，获取报告基本信息正常
input01 = {
    "certNo": "530322199005292217"
}
##获取报告基本信息正常
output01 ={
    "status": "0",
    "msg": "success",
    "data": {
        "result": "{\"ReportID\":209.0,\"ReportSn\":\"2017062900004139875112\",\"ReportCreateTime\":\"2017-06-29T16:06:34\",\"SourceType\":11}",
        "statusCode": "0",
        "statusDescription": "成功"
     }
}

##case02:
##验证不指定certNo时，获取报告基本信息异常
input02 = {
    "certNo": ""
}
##不输入身份证号，获取内容为空
output02 ={
    "status": "1",
    "msg": "证件号不能为空",
    "data": ""
}

##case03:
##验证输入无效的certNo时，获取报告基本信息异常
input03 = {
    "certNo": "123456"
}
##输入无效的身份证号，获取内容为空
output03 ={
    "status": "0",
    "msg": "success",
    "data": {
        "result": None,
        "statusCode": "1",
        "statusDescription": "征信报告信息不存在或者已经过期"
     }
}
