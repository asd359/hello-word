#coding:utf-8
import  urllib2,urllib,re
# from bs4 import  beautifulsoup
url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1481983328661_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&f=3&oq=mein&rsp=0"

html = urllib2.urlopen(url).read()
img = re.findall(r'"objURL":"(.*?)"',html)
print img

index = 0
# print str(index)
for url in img:
    if  index < 10:
        urllib.urlretrieve(url,'img'+str(index)+'.jpg')
        index+=1
    else:
        print "ok"
        break
