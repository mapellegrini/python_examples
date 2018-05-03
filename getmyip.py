#!/usr/bin/python

import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
response = opener.open("https://www.whatismyip.com/")
html = response.read()

pos=html.find("Your Public IPv4 is: ")
if (pos != -1):
  pos=pos+len("Your Public IPv4 is: ")
  pos2=html.find("</h3>", pos)
  ip = html[pos:pos2]
  print ip 
else:
  print "Could not determine ip" 


