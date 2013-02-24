#!/usr/bin/env python
from __future__ import print_function
from ConfigParser import SafeConfigParser
from markdown import markdown
import sys
import requests

#parse some commandline arguments
if sys.argv[1]==None:
    exit()

input = sys.argv[1]

with open(input,"r") as f:
    html = markdown(f.read())
    f.close()

with open('output.html','w') as f:
    f.write(html)
    f.close()
    print("written: %s" % 'output.html')

#parse configfile to wordpress
parser = SafeConfigParser()
parser.read('config.ini')

siteurl = parser.get('wordpress_site','site')
username = parser.get('wordpress_site','username')
password = parser.get('wordpress_site','password')

print (siteurl, username, password, sep="\n")
#parse the markdown file to html

#send the parsed html to wordpress
