#!/usr/bin/env python
from __future__ import print_function
from ConfigParser import SafeConfigParser
from markdown import markdown
import sys
from wordpress_xmlrpc import WordPressPost, Client
from wordpress_xmlrpc.methods.posts import NewPost

#TODO: change this part to optionparser
if sys.argv[1]==None:
    print("missing input file")
    exit()

input = sys.argv[1]

with open(input,"r") as f:
    #TODO: add try block to check for encoded strings or files and then use codecs to open
    html = markdown(f.read())
    f.close()
#parse the markdown file to html
# with open('output.html','w') as f:
#     f.write(html)
#     f.close()
#     print("written: %s" % 'output.html')

#parse configfile to wordpress
#TODO: add an option to use commandline args instead of config file
parser = SafeConfigParser()
parser.read('config.ini')

siteurl = "%s/%s" % (parser.get('wordpress_site','site'),"xmlrpc.php")
username = parser.get('wordpress_site','username')
password = parser.get('wordpress_site','password')

print (siteurl, username, password, sep="\n")
#send the parsed html to wordpress
wp = Client(siteurl,username, password)
post = WordPressPost()
if sys.argv[2]:
    post.title = sys.argv[2]
else:
    post.title = 'A new draft post'
post.content = html
post.post_status = 'draft'

wp.call(NewPost(post))