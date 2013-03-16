#Push (Markdown) to wordpress

**currently basic functionality**

A simple, python based, commandline wordpress blogging tool.  
A commandline wrapper to publishing with markdown and wordpress-xmlrpc


##Version

[Version](Version.md)

##Techonology
Using:

1. [python-wordpress-xmlrpc](https://github.com/maxcutler/python-wordpress-xmlrpc)  
2. [python-markdown](https://github.com/waylan/Python-Markdown)  

using wordpress:
[XML-RPC Api](http://codex.wordpress.org/XML-RPC_WordPress_API)  

##Installing
**The short way**:
Straight from the cheeseshop

    pip install push_to_wordpress

**The long way**:


    git clone git://github.com/alonisser/PushToWordpress.git

    cd PushToWordpress
    python setup.py install #(If that doesn't work you should run the build command first)


##Usage:
Current and quite basic:

    presser --title optionaltitle --posts inputfile.md anotherinputfile

where there is a config.ini file with wordpress blog connection details in the same folder. 

**Full command line options and flags** [here](usage.txt)

Simple isn't it?  
currently can't handle media files with the posts  
but check the TODO section for more info about that..

Don't forget to enter your wordpress blog config in the config.ini file (look at configdemo.ini for inspiration)

##License 
See [License](License.md)

##TODO or "How can I help or contribute":

fork, open issues etc. 
Don't forget to check our [TODO](TODO.md)

##Notice:

for older wordpress installs you should enable the XML-RPC [here](http://codex.wordpress.org/XML-RPC_Support)  
in later Wordpress versions it's enabled by default.