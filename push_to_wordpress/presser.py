#!/usr/bin/env python
from __future__ import print_function
from ConfigParser import SafeConfigParser
from ConfigParser import NoSectionError, NoOptionError
from markdown import markdown
import os
from wordpress_xmlrpc import WordPressPost, Client
from wordpress_xmlrpc.methods.posts import NewPost
import argparse

def read_config(configuration_parser):
    cparser = configuration_parser
    siteurl = "%s/%s" % (cparser.get('wordpress_site','site'),"xmlrpc.php")
    username = cparser.get('wordpress_site','username')
    password = cparser.get('wordpress_site','password')
    return (siteurl, username, password)


def presser():
    parser = argparse.ArgumentParser(description='presser - to push wordpress posts from the commandline')
    parser.add_argument('--config', action='store', dest='configfile',default=None)
    parser.add_argument('--title', action='store', dest='title', default='A new post' )
    parser.add_argument('--posts', help='a space seperated list of post names', default=[], dest='posts_to_process',nargs='+')
    parser.add_argument('--status', choices=('draft', 'publish','private'),help='post status defaults to %(default)s', default='draft', dest='status')
    # parser.add_argument('--siturl', action='store', dest='siteurl', help="the siteurl without xmlrpc overrides the config file" )
    # parser.add_argument('--username', action='store', dest='username', help="the username overrides the config file")
    # parser.add_argument('--password', action='store', dest='password', help="the password overrides the config file")
    # parser.add_argument('help')
    options = parser.parse_args()
    
    #parse configfile to wordpress
    #TODO: add an option to use commandline args instead of config file
    cparser = SafeConfigParser()
    try: #if there is a config options
        cparser.read(options.configfile)
        siteurl, username, password = read_config(cparser)
    except TypeError:
        try:
            configpath = os.path.dirname(os.path.abspath("__file__"))
            cparser.read(os.path.join(configpath,'config.ini'))
            siteurl, username, password = read_config(cparser)
        except (NoSectionError, NoOptionError):
            print("missing configuration information or file")
            import getpass
            siteurl = '%s/%s' % (raw_input("Full site url: "),"xmlrpc.php")
            username = raw_input("Wordpress site username: ")
            password = getpass.getpass("Enter wordpress site password: ")
    
    # TODO: check for missing configs

    print ('connection settings:', siteurl, username, password, sep="\n")
    #send the parsed html to wordpress
    wp = Client(siteurl,username, password)

    for p in options.posts_to_process:
        with open(p,"r") as f:
            #TODO: add try block to check for encoded strings or files and then use codecs to open
            html = markdown(f.read())
            f.close()

        post = WordPressPost()
        post.title =options.title
        post.content = html
        post.post_status = options.status

        wp.call(NewPost(post))
        print ('Done uploading: %s' % p)

if __name__ == '__main__':
   presser()