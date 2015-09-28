# -*- coding: UTF-8 -*-

import re
print(re.match('www','www.runoob.com').span())
print(re.match('com','www.runoob.com'))

line='Cats are smarter than dogs'
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

