#!/usr/bin/env python
# coding=utf-8
import json
import re

config = '''
	{
        "chushou":{
            "hdl":{
                "host":"jslive-hdl.kascend.com",
                "publish":""
            }
        },
        "gifshow":{
            "hdl":{
                "host":"gifshow.hdllive.ks-cdn.com",
                "publish":""
            }
        },
        "acgvideo":{
            "hdl":{
                "host":"js.live-play.acgvideo.com",
                "publish":""
            }
        },
        "panda":{
            "hdl":{
                "host":"pl30.live.panda.tv",
                "publish":""
            }
        }
    }
'''


def is_json(str):
	try:
		json.loads(str)
	except ValueError:
		return False
	return True

def parse():
	pattern = re.compile(r'^.*auth.*$')
	pattern_hdl = re.compile(r'^.*hdl.*$')
	pattern_rtmp = re.compile(r'^.*rtmp.*$')
	pattern_uplive = re.compile(r'^.*uplive.*$')

	for line in open("../conf/lua.conf"):
		if is_json(line):
			if(pattern.match(line)):
				s = json.loads(line)
				if(pattern_hdl.match(s["host"])):
					if("live" in s["conf"]["apps"][0].keys()):
						print "live"
					#elif:
						#print "app is not live"
				elif(pattern_rtmp.match(s["host"])):
					print "rtmp " + s["host"]
    	else:
    		print "valid json format" + ": " + line
if __name__ == "__main__":
	parse()