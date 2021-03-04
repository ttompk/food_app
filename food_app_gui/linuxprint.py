! /usr/bin/python
import os

os.system("lpr -P printer_name file_name.txt")
# "printer_name" represents the name of the printer you use on your system
# "file_name.txt"  is the name of the text file used for printing


# another version to try if above fails
'''
from subprocess import Popen
from cStringIO import StringIO

# place the output in a file like object
sio = StringIO(output_string)

# call the system's lpr command
p = Popen(["lpr"], stdin=sio, shell=True)
output = p.communicate()[0]
'''