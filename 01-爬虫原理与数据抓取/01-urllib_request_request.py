import urllib.request

# 字典格式！！
ua_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

# 网址最后的斜杠表示根目录，不要漏掉`
request = urllib.request.Request("http://www.baidu.com/", headers=ua_header)

response = urllib.request.urlopen(url=request)

html = response.read()

# print(html)
print(response.getcode())
print(response.geturl())
print(response.info())
