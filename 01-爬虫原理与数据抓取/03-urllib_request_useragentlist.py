import urllib.request
import random


ualist_header = [
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

url = "http://www.baidu.com/"
user_agent = random.choice(ualist_header)

# 网址最后的斜杠表示根目录，不要漏掉`
request = urllib.request.Request(url)
request.add_header("User-Agent", user_agent)

# 记住第一个字符大写，之后小写！！
print(request.get_header('User-agent'))
