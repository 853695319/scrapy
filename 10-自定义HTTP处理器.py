import urllib.request

# 1 构建HTTPHandle处理http请求
http_handle = urllib.request.HTTPHandler()

# 2 构建自定义opener
opener = urllib.request.build_opener(http_handle)

request = urllib.request.Request("http://www.baidu.com/")

# 3 用自定义opener处理http请求
response = opener.open(request)

# 4 输出结果
print(response.read().decode())
