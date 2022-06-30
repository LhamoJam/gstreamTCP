# INFO
Get gstreamer video and push cv2 image as TCP client
这个代码用来拉取gstreamer的视频流, 并且作为TCP客户端, 将视频数据发送出去

# 依赖
+ 只支持python 2.7 3.0-3.4
+ pygobject `python -c "import gi"`测试是否安装

# 安装
+ 安装 pygobject 使用 [PyGObject for Windows download |SourceForge.net](https://sourceforge.net/projects/pygobjectwin32/)

# 配置
+ `main.py`配置`host` `port`