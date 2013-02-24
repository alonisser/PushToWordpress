#Push (Markdown) to wordpress

**very early stage of design!**

A simple commandline blogging tool for python. A commandline wrapper to publishing

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

##TODO or "How can I help":

* add tests
* implents TODOs in presser.py
* make a setup script that installs this as a command line tool in python/[bin,scripts] !
* add docs