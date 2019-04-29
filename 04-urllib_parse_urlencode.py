import urllib.parse


wd = {"wd": "中文"}

# 该方法用于GET方法查询字符串的产生, 转码
result = urllib.parse.urlencode(wd)

print(result)

# 解码 urllib.parse.unquote()
org = urllib.parse.unquote(result)

print(org)
