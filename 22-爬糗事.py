"""
第一步 分析网页

url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)

# 作为根节点
article_box = $x('//div[contains(@id, "qiushi_tag_")]')

# username
./div[1]/a[2]/h2

# content
.//div[@class="content"]/span[1]

# 点赞
.//div[@class="stats"]/span[1]//i

# 评论
.//div[@class="stats"]/span[2]//i
"""
import json

import requests
from lxml import etree


def spider_qiushi(html):
    """
    解析网页，并将解析内容写入到qiushi.json
    :param html: string 网页源码
    :return:
    """
    xml = etree.HTML(html)
    article_box = xml.xpath('//div[contains(@id, "qiushi_tag_")]')
    item = {}
    for article in article_box:
        username = article.xpath('./div[1]/a[2]/h2')[0].text.strip()
        username = article.xpath('./div[1]/a[2]/h2')[0].text.strip()
        content = article.xpath('.//div[@class="content"]/span[1]')[0].text.strip()
        goodpoint = article.xpath('.//div[@class="stats"]/span[1]//i')[0].text.strip()
        comment = article.xpath('.//div[@class="stats"]/span[2]//i')[0].text.strip()

        item = {
            'username': username,
            'content': content,
            'goodpoint': goodpoint,
            "comment": comment
        }

        with open('qiushi.json', 'a') as fw:
            fw.write(
                json.dumps(item, ensure_ascii=False) + '\n'
            )
    print('ok')


def main():
    page = 2
    url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
    ua_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    response = requests.get(url, headers=ua_header)
    print("status_code:%d" % response.status_code)
    html = response.text


    spider_qiushi(html)


if __name__ == "__mian__":
    main()