import urllib.request


request = urllib.request.Request("http://www.baidu.com/")

# 1 构建HTTPHandle处理http请求
# dbbuglever 打开debug log 模式， 程序会执行的时候会打印收发包的信息,注释到 4 print
http_handle = urllib.request.HTTPHandler(debuglevel=1)

# 2 构建自定义opener
opener = urllib.request.build_opener(http_handle)

# 3 用自定义opener返回http响应
response = opener.open(request)

# 4 输出结果
# print(response.read().decode())
