#coding:utf-8
import re
str1 = "asdfj13812345678915869047163192.168.11.2，138.7.2.53323,34.5"
print re.findall(r'138\d{8}',str1)
print re.findall(r'158\d{8}',str1)

print re.findall(r'(([25[0-5]|2[0-5]\d|1\d\d|[1-9]\d|[1-9])\.){1,3}([25[0-5]|2[0-5]\d|1\d\d|[1-9]\d|[1-9])',str1)


import  time
