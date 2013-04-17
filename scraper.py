'''
Created on Apr 17, 2013

@author: sebastian
'''

import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open("http://en.wikipedia.org/wiki/Django_web_framework")
page_content = response.read();

print page_content 
