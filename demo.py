# -*- coding:utf-8 -*-
import urllib2

# 直接请求
response = urllib2.urlopen('http://www.baidu.com')

# 获取状态码，如果是200表示获取成功
print response.getcode()

# 读取内容
cont = response.read()

print cont