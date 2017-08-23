#!/usr/bin/env python
# coding=utf-8

import subprocess

class myutils:
	def __init__(self):
		pass

	def execute_cmdLine(self, cmdLine):
	    p = subprocess.Popen(cmdLine, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,shell=True);
	    stdout,stderr = p.communicate()
	    print "---------------------"
	    print stdout
	    print "================"
	    print stderr
	    print "---------------"
	    if p.returncode != 0:
	        raise RuntimeError("%r failed, status code %s stdout %r stderr %r" % (cmdLine, p.returncode, stdout, stderr))
	        return -1;
	    return stdout,stderr;

	def run(self, cmdLine):
	    print(cmdLine)
	    subprocess.call(cmdLine, shell=True)