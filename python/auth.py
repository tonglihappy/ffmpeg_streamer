#!/usr/bin/env python
# coding=utf-8

import hashlib
import time
import json

class auth:
	def __init__(self):
		pass

	def get_url_md5(self, url, key, time_out, param_key, param_time, md5_start_pos, md5_len):
		if isinstance(key, str) and isinstance(time_out, int) and isinstance(param_key, str) and isinstance(param_time, str):
			param_time = param_time + "=" + str(time.time() + time_out).split(".")[0]
			param_key = param_key + "=" + hashlib.md5((key + param_time).encode('utf-8')).hexdigest()
		else:
			print "Check the correctness of input parameters of get_url_md5"
		return url + "?" + param_key + "&" + param_time

if __name__ == '__main__':
	a = auth()
	url = a.get_url_md5("url", '124', 60, "ks", "ts", 0, 32)

	print url