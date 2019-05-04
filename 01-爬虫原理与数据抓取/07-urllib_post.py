import urllib.request
import urllib.parse

"""
目的：学习POST方式


POST https://fanyi.baidu.com/v2transapi HTTP/1.1
Host: fanyi.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://fanyi.baidu.com/?aldtype=16047
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 121
Connection: keep-alive
Cookie: BAIDUID=CAD28827099BE88F67EC86DC33EEB368:FG=1; BIDUPSID=CAD28827099BE88F67EC86DC33EEB368; PSTM=1556418486; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1464_21096_28721_28832_28584; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1556505103,1556509798,1556509836; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1556509836; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; delPer=0; PSINO=7; locale=zh

from=en
to=zh
query=query
transtype=realtime
simple_means_flag=3
sign=83774.369679
token=649d104fe64f36f71148f1c87c183954
"""

url = "https://fanyi.baidu.com/v2transapi"
# query = input("请输入翻译关键字：")
form_data = {
    "from": "zh",
    "to": "en",
    "query": "这里",
    "transtype": "realtime",
    # "simple_means_flag": "3",
    "sign": "162854.433943",
    "token": "649d104fe64f36f71148f1c87c183954",
}
# 注意 post的body 数据要全部进行转码
data = urllib.parse.urlencode(form_data).encode()
header = {
    "Host": "fanyi.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "*/*",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    # cookie是一定要的
    "Cookie": "BAIDUID=CAD28827099BE88F67EC86DC33EEB368:FG=1; BIDUPSID=CAD28827099BE88F67EC86DC33EEB368; PSTM=1556418486; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1464_21096_28721_28832_28584; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1556505103,1556509798,1556509836; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1556509836; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; delPer=0; PSINO=7; locale=zh"
}

request = urllib.request.Request(url, data=data, headers=header)
reponse = urllib.request.urlopen(request)
print("code:{}\nurl:{}\n".format(reponse.getcode(), reponse.geturl()))
print("-"*20)
print(reponse.read())
