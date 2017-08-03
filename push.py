#!/usr/bin/env python

import subprocess

def run(cmdLine):
	print(cmdLine)
	subprocess.call(cmdLine, shell=True)


if __name__ == "__main__":
	print("hello")

