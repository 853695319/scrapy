import json

import requests
import jsonpath
import chardet

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
response = requests.get(url, headers=headers)
# print(response)  # for test
data_json = json.loads(response.text)  # 默认Unicode，如果传入其他编码gbk，需要指定encoding='gbk'
# print(type(data_json))
city_list = jsonpath.jsonpath(data_json, '$..name')
# for city in city_list:
#     print(city)
json.dump(city_list, open('city_list.json', 'w', encoding='utf-8'), ensure_ascii=False)