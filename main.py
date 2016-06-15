# -*- coding: UTF-8 -*-
import login
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

username = raw_input(u'请输入用户名：')
password = raw_input(u'请输入密码：')
mylog = login.log_in(username, password)
mylog.login()

# 测试登录成功，云飞雪逸的主页URL
myUrl = 'http://weibo.com/u/3205309050?from=page_100505_profile&wvr=6&mod=like&is_all=1'
res = urllib2.urlopen(myUrl)
data = res.read()
res.close()
data = data.decode('utf-8')
print data

f = file('weibo.txt', 'a')
f.write(data)
f.close()
