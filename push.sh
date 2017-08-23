./ffmpeg -k -re -stream_loop 10 -i ~/ss.flv -acodec aac -vcodec h264 -r 9 -f flv rtmp://112.84.134.61/livecdn-qa-online.uplive.kscvbu.cn/live/test008
