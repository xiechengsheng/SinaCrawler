# -*- coding: UTF-8 -*-

import urllib2
import re
import json
import string

'''
class GET_DATA:
    def __init__(self):
        # 获取servertime ,nonce ,publey,rsakv的网址
        self.url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1398760051250'

    def get_data(self):
        data = urllib2.urlopen(self.url).read()
        print data
        p = re.compile('(.∗)')
        try:
            json_data = p.search(data).group(1)
            print json_data
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakv = data['rsakv']
            return nonce,rsakv,servertime,pubkey
        except:
            print '不能获取servertime 和 data'
            return None
'''


class GET_DATA:
    def __init__(self):
        # 获取servertime ,nonce ,publey,rsakv的网址
        self.url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1398760051250'

    def get_data(self):
        data = urllib2.urlopen(self.url).read()
        print data
        # p = re.compile('(.∗)')
        try:
            p = re.compile(r'"servertime":(.*?),', re.S)
            servertimeAll = p.findall(data)
            servertime = servertimeAll[0]
            print servertime
            p = re.compile(r'"nonce":(.*?),', re.S)
            nonceAll = p.findall(data)
            nonce = nonceAll[0][1:-1]
            print nonce
            p = re.compile(r'"pubkey":(.*?),', re.S)
            pubkeyAll = p.findall(data)
            pubkey = pubkeyAll[0][1:-1]
            print pubkey
            p = re.compile(r'"rsakv":(.*?),', re.S)
            rsakvAll = p.findall(data)
            rsakv = rsakvAll[0][1:-1]
            print rsakv
            return nonce, rsakv, servertime, pubkey
        except:
            print '不能获取servertime 和 data'
            return None
