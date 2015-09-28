__author__ = 'Sun'
import urllib
import urllib2
import re
import time, datetime
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

format_str = '%Y-%m-%d %H:%M:%S'
url = 'http://neihanshequ.com/'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8', 'ignore')
    pattern = re.compile(
        '<div.*?' + 'content-wrapper">.*?<p>(.*?)</p>',
        re.S)
    items = re.findall(pattern, content)
    i=1
    file=open('html.html','w')
    file.write(content)
    file.close()
    for item in items:
        its=item.replace('<br />','')
        itss=str(i)+'.'+its
        i=i+1
        print itss
        print
        f=open('duanzi.txt','a')
        f.write('\n')
        f.write('\n')
        f.write(itss)
        f.close()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "resson"):
        print e.reason
