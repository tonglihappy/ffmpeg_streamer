#!/usr/bin/env python
# coding=utf-8

import unittest
import platform

import auth
import stream
import myutils

class mytest(unittest.TestCase):
    def setUp(self):
    	self.utils = myutils.myutils()
        self.auth = auth.auth()
        pass

    def tearDown(self):
        pass

    #def test_push_stream(self):
    	#url = "../ffmpeg -re -i ~/ss.flv -acodec copy -vcodec copy -f flv rtmp://14.17.124.23/livecdn-qa-online.uplive.kscvbu.cn/live/test008"
        #self.utils.execute_cmdLine(url)
        #pass

    def test_pull_stream(self):
        if(platform.system() == "Windows"):
            url =  self.auth.get_url_md5("url", '124', 60, "ks", "ts")
            stderr , stdout = self.utils.execute_cmdLine("wget " + "http://112.84.134.61/livecdn-qa-online.hdllive.kscvbu.cn/live/test008.flv")
            print "hello"
            print stderr, stdout
        else:
            url =  self.auth.get_url_md5("url", '124', 60, "ks", "ts")
            stdout, stderr = self.utils.execute_cmdLine("wget " + "http://112.84.134.61/livecdn-qa-online.hdllive.kscvbu.cn/live/test008.flv")
            #print "hello"
            #print stderr, stdout

if __name__ == "__main__":
    unittest.main()
