#!/usr/bin/env python
# coding=utf-8

import subprocess
import os
import re
import string
import threading
from multiprocessing import cpu_count
from collections import OrderedDict

base_dir = ""

def run(cmdLine):
	subprocess.call(cmdLine, shell=True)

def mem_info():
	meminfo = OrderedDict()
	with open('/proc/meminfo') as f:
		for line in f:
			meminfo[line.split(':')[0]] = line.split(':')[1].strip()
	return meminfo

def compile_srs(srs_path):
	os.chdir(srs_path)
	run("./configure && make")

def	init_st_load():
	os.chdir(base_dir)
	srs_path = "./srs-bench"
	if os.path.isdir(srs_path):
		pass
	else:
		run("git clone https://github.com/ossrs/srs-bench.git")
		compile_srs(srs_path)

def strateg_stress():
	cpucount = cpu_count()
	meminfo = mem_info()
	memcount =  string.atoi(meminfo['MemTotal'].split(" ")[0]) / 1000000
	#if(memcount > 10 )

def stress_pull(url):
	os.chdir(base_dir)
	os.chdir("./srs-bench/objs")
	pattern_hdl = re.compile(r'^.*hdl.*$')
	pattern_hls = re.compile(r'^.*hls.*$')
	match_hdl = pattern_hdl.match(url)
	match_hls = pattern_hls.match(url)

	if(url.split(":")[0] == "rtmp"):
		if(os.path.exists(r'./sb_rtmp_load')):
			run("./sb_rtmp_load" + " -c " + str(5) + " -r " + url)
		else:
			print "sb_rtmp_load not exists"
	elif(url.split(":")[0] == "http" and match_hdl):
		if(os.path.exists(r'./sb_http_load')):
			run("./sb_http_load" + " -c " + str(5) + " -r " + url)
		else:
			print "sb_http_load not exists"
	elif(url.split(":")[0] == "http" and match_hls):
		if(os.path.exists(r'./sb_hls_load')):
			run("./sb_hls_load" + " -c " + str(5) + " -r " + url)
		else:
			print "sb_hls_load not exists"
	pass

def run_push_stream(url, s_num, filename):
	os.chdir(base_dir)
	os.chdir("./srs-bench/objs")
	if(os.path.exists(r'./sb_rtmp_publish')):
		if(s_num <= 1):
			run("./sb_rtmp_publish -i " + filename + " -c " + str(s_num) + " -r " + url)
		else:
			run("./sb_rtmp_publish -i " + filename + " -c " + str(s_num) + " -r " + url + "_{i}")
	else:
		print "file not exists"
	pass

def stress_push(url, s_num, filename):
	t1 = threading.Thread(target=run_push_stream, args=(url, s_num, filename))
	t1.start()
	pass

if __name__ == '__main__':
	push_stream = True
	pull_stream = True
	push_url = "rtmp://14.17.124.23/livecdn-qa-online.uplive.kscvbu.cn/live/test008"
	pull_url = "rtmp://14.17.124.23/livecdn-qa-online.rtmplive.kscvbu.cn/live/test008"
	source_file_name = "ss.flv"

	base_dir = os.getcwd()

	init_st_load()

	#推流需要有s_num推流路数，拉流根据服务器性能计算出拉流策略
	if(push_stream):
		stress_push(push_url, 1, source_file_name)

	if(pull_stream):
		stress_pull(pull_url)