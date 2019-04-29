import urllib.request
import urllib.parse


"""
GET https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1 HTTP/1.1

Host: movie.douban.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: bid=cvRdirp_XjE
Upgrade-Insecure-Requests: 1
"""

url = "https://movie.douban.com/j/chart/top_list?"
query_string = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    # ajax get
    "start": "0",
    "limit": "1"
}
fullurl = url + urllib.parse.urlencode(query_string)
# ajax post
form_data = {
    "start": "0",
    "limit": "1"
}
data = urllib.parse.urlencode(form_data).encode()
header = {
    # "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Cookie": "bid=cvRdirp_XjE",
    # "Upgrade-Insecure-Requests": "1",
}

# ajax post
# request = urllib.request.Request(fullurl, data=data, headers=header)

# ajax get
request = urllib.request.Request(fullurl, headers=header)

# 上面两种方法都可行

reponse = urllib.request.urlopen(request)

print("code:{}\nurl:{}\n".format(reponse.getcode(), reponse.geturl()))
print("-"*20)
print(reponse.read())  # 在win平台默认gbk编码，输出的时候很麻烦
# print(reponse.read().decode())  # python3 08-urllib_ajax.py > douban.json linux平台可以做到，win不可以
