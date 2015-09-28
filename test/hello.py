__author__ = 'Sun'
import urllib
import urllib2
import re
import time,datetime
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

request=urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
    print e.reason

page=1
format_str='%Y-%m-%d %H:%M:%S'
url='http://www.qiushibaike.com/hot/page/'+str(page)
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    content=response.read().decode('utf-8','ignore')
    pattern=re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items=re.findall(pattern,content)
    for item in items:
        haveImg=re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],time.strftime(format_str,time.localtime(float(item[2]))),item[4]
            f=open('qiushibaike.txt','a')
            f.write(item[0].rstrip())
            f.write(item[1])
            f.write(time.strftime(format_str,time.localtime(float(item[2]))))
            f.write(item[4])
            f.close()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"resson"):
        print e.reason
