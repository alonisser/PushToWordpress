#Push (Markdown) to wordpress

**very early stage of design!**

A simple, python based, commandline wordpress blogging tool.  
A commandline wrapper to publishing with [python-markdown](https://github.com/waylan/Python-Markdown)

first iteration

##Techonology
Using:

1. [python-wordpress-xmlrpc](https://github.com/maxcutler/python-wordpress-xmlrpc)  
2. [python-markdown](https://github.com/waylan/Python-Markdown)  

using wordpress [XML-RPC Api](http://codex.wordpress.org/XML-RPC_WordPress_API) to drive wordpress.


##Installing
currently:


    git clone this repo
    cd repo folder
    python setup.py install (If that doesn't work you should run the build command first)

working on a 'pip install' version, straight from the cheeseshop  

##Usage:
Current and quite basic:

    presser --title optionaltitle --posts inputfile.md anotherinputfile

where there is a config.ini file with wordpress blog connection details in the same folder. 

**[Full command line options and flags](usage.txt)**

Simple isn't it? going to be simpler soon..  
currently can't handle media files with the posts (but check the TODO section for more info about that).
Don't forget to enter your wordpress blog config in the config.ini file (look at configdemo.ini for inspiration)

[License](License.md)
##TODO or "How can I help":

check our [TODO](TODO.md)

##Notice:

for older wordpress installs you should enable [enable the XML-RPC api](http://codex.wordpress.org/XML-RPC_Support) in later versions it's enabled by default.