#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

##签章二期接口的请求database定义
host = '10.139.60.153'
user = 'sa'
pwd = '123456@'
db = 'kkdcfca'

##申请合同签章（多个签章/签名）接口的请求路径定义
ad_applyMultiple = '/micro/cfca/seal/apply/multiple'

##取得合同（按签章申请ID）接口的请求路径定义
ad_retrieve = '/micro/cfca/seal/retrieve'

##最大轮询次数
maxjob_cnt = 5

#CaseNo10501
#异步请求申请10个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput01 = [
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed201",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"kkd_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":300
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":150,
            "Ly":330
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed202",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uANgMiAADBwmNe2tw121.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed203",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAIRocAAK74VemLYs968.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":80
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":80
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed204",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAWgClAAEJ2SFKo4Q822.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"zyxj_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":200,
            "Ly":150
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed205",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAUj-LAAELPf7ptec866.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"zyxj_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":650
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":650
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed206",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAXS0mAAEZ3ed9tb4917.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":200
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed207",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAOOYdAADUapqooQw189.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed208",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":200,
            "Ly":200
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed209",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAXFRTAA_GjI_qDVQ545.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":164,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":164,
            "Lx":200,
            "Ly":200
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed210",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":400
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":300,
            "Ly":400
        }
    ],
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

##applyMultiple接口所需要提供的输出数据  ,方便进行比对  data output
applyMultipleOutput01 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 10,
  "SuccessCount": 10,
  "ContractApplyResponseList": []
}

#CaseNo10502
#异步请求申请1个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput02 = [
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f600010",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"kkd_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
            "UserName":"赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-18",
            "SignLocation":"北京",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":150,
            "Ly":150
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyMultipleOutput02 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}

#CaseNo10503
#异步请求申请5个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput03 = [
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed206",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAXS0mAAEZ3ed9tb4917.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed207",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAOOYdAADUapqooQw189.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed208",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed209",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAXFRTAA_GjI_qDVQ545.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":164,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":164,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed210",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":400
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":300,
            "Ly":400
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyMultipleOutput03 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 5,
  "SuccessCount": 5,
  "ContractApplyResponseList": []
}

#CaseNo10504
#异步请求申请20个合同签章/签名,每个合同同时指定一个有效印章和一个有效签名
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput04 = [
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed401",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAA7zOAACIjz4udoc485.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"kkd_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":300
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":150,
            "Ly":330
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed402",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uANgMiAADBwmNe2tw121.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "Async":"false",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed403",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAIRocAAK74VemLYs968.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":80
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/41/Cos8o1oefOOABD-DAAAKIHMC2Uw739.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":80
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed404",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9uAWgClAAEJ2SFKo4Q822.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"zyxj_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":200,
            "Ly":150
        }
    ],
    "Async":"false",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed405",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAUj-LAAELPf7ptec866.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"zyxj_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":650
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":650
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed406",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAXS0mAAEZ3ed9tb4917.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed407",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAOOYdAADUapqooQw189.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed408",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed409",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAXFRTAA_GjI_qDVQ545.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":164,
            "Lx":400,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":164,
            "Lx":200,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"wxjkTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed410",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAHKCSAAFJYSnEmzo465.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":400
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":300,
            "Ly":400
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed411",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAK0C9AADYsvq7AUo967.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":600
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed412",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAUJ--AAKiJk2TLck355.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":100
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":150,
            "Ly":100
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed413",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAZiVXAADQDMUupmI809.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":150,
            "Ly":150
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed414",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAYIGWAAEyBg3bXbQ135.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":300
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":150,
            "Ly":300
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed415",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yANr4OAATvM6MUAdY819.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":8,
            "Lx":400,
            "Ly":650
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":8,
            "Lx":150,
            "Ly":650
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed416",
    "PdfDfsRelPath":"group1/M00/2F/CE/Cos8o1oyP9yAGMFEAAWHpNPjr8s251.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":5,
            "Lx":400,
            "Ly":170
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":5,
            "Lx":200,
            "Ly":170
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed417",
    "PdfDfsRelPath":"group1/M00/2F/41/Cos8o1oeeSiAVp5WAAQBFrNWcGg471.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":150
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed418",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6T-AKnHxAAh6lLbbfP8900.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":5,
            "Lx":400,
            "Ly":600
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":5,
            "Lx":150,
            "Ly":600
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed419",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ZmAA8vfAALY50h3ydE681.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":1,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6ouAXG5WAAAWxwqodUM659.jpg",
            "UserName":"tony赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":1,
            "Lx":170,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
},
{
    "Account":"zyxjTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f4ed420",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yALQ8BAAD0ahsqlB0891.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"wxjk_seal",
            "Pagen":2,
            "Lx":350,
            "Ly":200
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CD/Cos8o1ox6kGABwsOAAAvLLJZijA679.jpg",
            "UserName":"黄婷婷",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-19",
            "SignLocation":"纽约",
            "SignReason":"签约授权",
            "Pagen":2,
            "Lx":150,
            "Ly":200
        }
    ],
    "Async":"true",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyMultipleOutput04 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 20,
  "SuccessCount": 20,
  "ContractApplyResponseList": []
}

#CaseNo10505
#按签章申请ID,取得合同
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput05 = {
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "SealApplyId":""
}


applyMultipleOutput05 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 20,
  "SuccessCount": 20,
  "ContractApplyResponseList": []
}

#CaseNo10506
#同步请求申请1个合同签章/签名,
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput06 = [
{
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "LoanKind":"LOANKIND/KAKADAI",
    "ContractNo":"3db2d300-312f-488b-81e3-70a15f600110",
    "PdfDfsRelPath":"group1/M00/2F/CD/Cos8o1oyP9yAJ2bvAAQymhdNcnQ988.pdf",
    "SealRequestList": [
         {
            "SealReason":"签约授权",
            "SealLocation":"北京",
            "OfficialSealCode":"kkd_seal",
            "Pagen":3,
            "Lx":400,
            "Ly":150
        }
    ],
    "SignatureRequestList": [
         {
            "HandWritingDfsRelPath":"group1/M00/2F/CE/Cos8o1oyQOGAPmkiAAEa2PYCOjw474.png",
            "UserName":"赵忠祥",
            "IdentificationNo":"211003199003212819",
            "UserPhone":"18012345678",
            "SignDate":"2017-12-18",
            "SignLocation":"北京",
            "SignReason":"签约授权",
            "Pagen":3,
            "Lx":150,
            "Ly":150
        }
    ],
    "Async":"false",
    "CallBackUrl":"http://10.139.60.154:9002/micro/cfca/seal/callback"
}
]

applyMultipleOutput06 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}


#CaseNo10507
#按签章申请ID,取得合同
#applyMultiple接口所需要提供的输入数据  data input
applyMultipleInput07 = {
    "Account":"kkdTester",
    "Password":"UGFzc3dvcmQxMjM=",
    "SealApplyId":""
}

applyMultipleOutput07 ={
  "Status": 1,
  "Message": "签章成功",
  "SealApplyId": "申请成功的ID",
  "SealApplyCount": 1,
  "SuccessCount": 1,
  "ContractApplyResponseList": []
}