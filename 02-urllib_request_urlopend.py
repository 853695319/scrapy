import urllib.request


request = urllib.request.urlopen(url="http://www.baidu.com/")

html = request.read()

print(html)
