#!/usr/bin/python
import codecs
import cgitb

cgitb.enable()
print("Content-Type: text/html\n")

f=codecs.open("index.html", 'r')
print (f.read())
