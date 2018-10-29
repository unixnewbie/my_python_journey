#!/usr/bin/python
import subprocess
def greet(name):
 upname=str.upper(name)
 namelen=len(name)
 lname=list(name)
 lname.reverse()
 rname=''.join(lname)
 print ("Hello {0}. You  have {1} characters in your name.Your name reversed is {2}").format (upname,namelen,str.upper(rname))
subprocess.call("clear",shell=True)
name=str(raw_input("Enter your name:"))
greet(name)
