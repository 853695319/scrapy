import urllib.request
import urllib.parse
import ssl


url = "https://www.baidu.com/"
ua_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}
# 忽略未认证SSL警告
# 一般都可以用HTTP发，但有些类是交易，金融网站就比较严格
context = ssl._create_unverified_context()

request = urllib.request.Request(url, headers=ua_header)
response = urllib.request.urlopen(request, context=context)

print(response.read().decode())
