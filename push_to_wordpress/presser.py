#!/usr/bin/env python
from __future__ import print_function
from ConfigParser import SafeConfigParser
from markdown import markdown
import sys
import os
from wordpress_xmlrpc import WordPressPost, Client
from wordpress_xmlrpc.methods.posts import NewPost

def presser():
    #TODO: change this part to optionparser
    if len(sys.argv) == 1 or sys.argv[1] is None:
        print ("missing input file")
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
    configpath = os.path.dirname(os.path.abspath("__file__"))
    parser.read(os.path.join(configpath,'config.ini'))

    siteurl = "%s/%s" % (parser.get('wordpress_site','site'),"xmlrpc.php")
    username = parser.get('wordpress_site','username')
    password = parser.get('wordpress_site','password')
    #TODO: check for missing configs

    print ('connection settings:', siteurl, username, password, sep="\n")
    #send the parsed html to wordpress
    wp = Client(siteurl,username, password)
    post = WordPressPost()
    try:
        post.title = sys.argv[2]
    except IndexError:
        post.title = 'A new draft post'
    post.content = html
    post.post_status = 'draft'

    wp.call(NewPost(post))

if __name__ == '__main__':
   presser()