#Push (Markdown) to wordpress

**very early stage of design!**

A simple, python based, commandline wordpress blogging tool.

A commandline wrapper to publishing with [python-markdown](https://github.com/waylan/Python-Markdown)

first iteration

##Techonology
Using:

[python-wordpress-xmlrpc](https://github.com/maxcutler/python-wordpress-xmlrpc)

[python-markdown](https://github.com/waylan/Python-Markdown)

using wordpress XML-RPC Api to drive wordpress


##Installing
pip install -r require.txt

##Usage:
basic:

    python presser.py inputfile.md optionaltitle

Simple isn't it? going to be simpler soon..

currently can't handle media files with the posts (but check the TODO section for more info about that).
Don't forget to enter your wordpress blog config in the config.ini file (look at configdemo.ini for inspiration)

##TODO or "How can I help":

* add tests
* implents TODOs in presser.py
* make a setup script that installs this as a command line tool in python/[bin,scripts] !
* add docs
* add option to upload plaintext files, html files, Rst files etc.
* add option to upload as markup without html processing
* add option to upload media files with the post
