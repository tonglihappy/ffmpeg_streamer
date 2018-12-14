## 直播测试时候修改的ffmpeg推流工具。
## 一.异常推流工具

我们这个工具是根据ffmpeg tools框架修改的，不影响ffmpeg原有的推拉流，转码功能，只是将我们的异常情况集成到了ffmpeg里面

## 使用方式：

1.git clone https://github.com/tonglihappy/ffmpeg_streamer.git

2.cd ffmpeg_streamer

3.make

## 场景：

### 1.卡顿流(每10s随机卡顿1s) -k

ffmpeg -k -re -i ss.flv -c copy -f flv url

### 2.纯视频 -vn

ffmpeg -re -i ss.flv -acodec copy -vn -f flv url

### 3.纯音频 -an

ffmpeg -re -i ss.flv -vcodec copy -an -f flv url

### 4.推流只有关键帧 -only_key

ffmpeg -only_key -re -i ss.flv -acodec  aac -vcodec h264 -f flv url

注意：

只推关键帧要注意设置帧率fps!

### 5.关键帧随机丢失 -key_loss + -only_key

ffmpeg -only_key -key_loss -re -i ss.flv -c copy -f flv url

### 6.只发特定数量的关键帧

ffmpeg -key_num:5 -re -i ss.flv -c copy -f flv url

### 7.随机丢关键帧

ffmpeg -key_loss -re -i ss.flv -c copy -f flv url


### 8.循环推流(文件读完不会中断连接，ffmpeg某些流stream_loop不会生效，此处做了修改)

ffmpeg -re -stream_loop 10 -i ss.flv -c copy -f flv url

经过测试，这个ffmpeg存在bug。并不是所有的文件都能循环。


