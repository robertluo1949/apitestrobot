#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
desctiption: 发送请求 & 解析response json
author: Emily
'''
import load_credit_yaml
import urllib2.request
import urllib.parse

class SendCreditRequest:
    def __init__(self):
        pass
    
    # return json format  
    def applyCreditRequest(self):
        lc= LoadFileSystempath()
        testIp=lc.getValue('testIp')
        testPort = lc.getValue('testPort')
        applyCreditReport = lc.getValue('applyCreditReport')
        getCreditReport = lc.getValue('getCreditReport')
        # TODO(Emily) get data from data_credit02.py
        data = json.dump(urllib.urlencode('data from data_credit02.py'))
        data = data.encode('utf-8')
        req = urllib2.Request(url, j_data, headers)
        req2 = urllib2.urlopen(req)
        res = json.loads(req2.read())
        req2.close()
        return res;