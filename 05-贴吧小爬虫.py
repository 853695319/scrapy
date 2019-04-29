import urllib.parse
import urllib.request

# 特别注意导入模块的方式
url = "https://www.baidu.com/baidu"
keyword = input("请输入要查询的字符串:")
wd = {'wd': keyword}
query = urllib.parse.urlencode(wd)
fullurl = url + "?" + query
ua_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}
request = urllib.request.Request(fullurl, headers=ua_header)
response = urllib.request.urlopen(request)
# 可以用抓包工具查看结果
# print(response.read())
# 200 成功，然后检查网址
print(response.getcode())
print(response.geturl())
