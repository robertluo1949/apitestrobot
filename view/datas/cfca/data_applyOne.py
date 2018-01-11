#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

##签章二期接口的请求database定义
host = '10.139.60.153'
user = 'sa'
pwd = '123456@'
db = 'kkdcfca'

##申请合同签章（一个签章/签名）接口的请求路径定义
ad_applyOne = '/micro/cfca/seal/apply'

##取得合同（按签章申请ID）接口的请求路径定义
ad_retrieve = '/micro/cfca/seal/retrieve'

##最大轮询次数
maxjob_cnt = 5

#CaseNo10511
#异步请求申请10个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyOne接口所需要提供的输入数据  data input
applyOneInput01 = [
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059001",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uANgMiAADBwmNe2tw121.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0002",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059002",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAWgClAAEJ2SFKo4Q822.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0003",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059003",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0004",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059004",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAK0C9AADYsvq7AUo967.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0005",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059005",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0006",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059006",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAZiVXAADQDMUupmI809.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0007",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059007",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAYIGWAAEyBg3bXbQ135.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0008",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059008",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yANr4OAATvM6MUAdY819.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0009",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059009",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAGMFEAAWHpNPjr8s251.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0010",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d059010",
    "pdfDfsRelPath":"group1/M00/2F/41/Cos8o1oeeSiAVp5WAAQBFrNWcGg471.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

##applyOne接口所需要提供的输出数据  ,方便进行比对  data output
applyOneOutput01 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 10,
  "SuccessCount": 10,
  "ContractApplyResponseList": []
}

#CaseNo10512
#异步请求申请1个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyOne接口所需要提供的输入数据  data input
applyOneInput02 = [
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d001001",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6T-AKnHxAAh6lLbbfP8900.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-21",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyOneOutput02 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}

#CaseNo10513
#异步请求申请5个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyOne接口所需要提供的输入数据  data input
applyOneInput03 = [
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d058001",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uANgMiAADBwmNe2tw121.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d058002",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAWgClAAEJ2SFKo4Q822.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d058003",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d058004",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAK0C9AADYsvq7AUo967.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d058005",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyOneOutput03 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 5,
  "SuccessCount": 5,
  "ContractApplyResponseList": []
}

#CaseNo10514
#异步请求申请20个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyOne接口所需要提供的输入数据  data input
applyOneInput04 = [
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060001",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uANgMiAADBwmNe2tw121.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0002",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060002",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAWgClAAEJ2SFKo4Q822.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0003",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060003",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0004",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060004",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAK0C9AADYsvq7AUo967.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0005",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060005",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0006",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060006",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAZiVXAADQDMUupmI809.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0007",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060007",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAYIGWAAEyBg3bXbQ135.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0008",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060008",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yANr4OAATvM6MUAdY819.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0009",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060009",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAGMFEAAWHpNPjr8s251.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0010",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060010",
    "pdfDfsRelPath":"group1/M00/2F/41/Cos8o1oeeSiAVp5WAAQBFrNWcGg471.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0003",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060011",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAXFRTAA_GjI_qDVQ545.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0004",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060012",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAIRocAAK74VemLYs968.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0005",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060013",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAUj-LAAELPf7ptec866.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0006",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060014",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAXS0mAAEZ3ed9tb4917.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"wxjkTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"WXJK",
    "contractTemplateCode":"T_WXJK_0007",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060015",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yALQ8BAAD0ahsqlB0891.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"zyxjTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"ZYXJ",
    "contractTemplateCode":"T_ZYXJ_0002",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060016",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"zyxjTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"ZYXJ",
    "contractTemplateCode":"T_ZYXJ_0003",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060017",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAOOYdAADUapqooQw189.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/30/07/Cos8o1o3ZlOAWMvGAAAWxwqodUM588.bmp",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"zyxjTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"ZYXJ",
    "contractTemplateCode":"T_ZYXJ_0004",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060018",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAUJ--AAKiJk2TLck355.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"zyxjTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"ZYXJ",
    "contractTemplateCode":"T_ZYXJ_0005",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060019",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6T-AKnHxAAh6lLbbfP8900.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "account":"zyxjTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"ZYXJ",
    "contractTemplateCode":"T_ZYXJ_0006",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d060020",
    "pdfDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ZmAA8vfAALY50h3ydE681.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-27",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"true",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyOneOutput04 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 20,
  "SuccessCount": 20,
  "ContractApplyResponseList": []
}

#CaseNo10515
#按签章申请ID,取得合同
#applyOne接口所需要提供的输入数据  data input
applyOneInput05 = {
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "SealApplyId":""
}


applyOneOutput05 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 20,
  "SuccessCount": 20,
  "ContractApplyResponseList": []
}

#CaseNo10516
#同步请求申请1个合同签章/签名,
#applyOne接口所需要提供的输入数据  data input
applyOneInput06 = [
{
    "account":"kkdTester",
    "password":"UGFzc3dvcmQxMjM=",
    "loanKind":"LOANKIND/KAKADAI",
    "channelCode":"KKD",
    "contractTemplateCode":"T_KKD_0001",
    "contractNo":"fd71e3b3-8ef3-416f-8773-608e8d001002",
    "pdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "sealRequest": {
        "sealName":"维信金科有限公司",
        "sealReason":"签约授权",
        "sealLocation":"上海"
    },
    "signatureRequest": {
        "handWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
        "userName":"王泓洋",
        "identificationNo":"211003199003212819",
        "userPhone":"18012345678",
        "signDate":"2017-12-21",
        "signLocation":"上海",
        "signReason":"签约授权"
    },
    "async":"false",
    "callBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyOneOutput06 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}

#CaseNo10517
#按签章申请ID,取得合同
#applyOne接口所需要提供的输入数据  data input
applyOneInput07 = {
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "SealApplyId":""
}


applyOneOutput07 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}
