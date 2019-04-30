import urllib.request
import urllib.parse
import time
import re
from functools import wraps

from lxml import etree

def deco_http2xml(func):
    @wraps(func)
    def wrapper(url, filename):
        # 获得html
        origin_html = func(url, filename)
        
        # 由于百度贴吧的页面被注释了，所以通过正则表达式预处理html
        main_html = re.sub(
            r'<!--|-->',
            "", origin_html
        )

        # 解析成HTML DOM 
        main_xml = etree.HTML(main_html)

        # 通过xpath提取帖子链接
        main_links = list(map(
            lambda x: 'https://tieba.baidu.com{}'.format(x),
            main_xml.xpath('//div[@class="threadlist_title pull_left j_th_tit "]//a[@class="j_th_tit "]/@href')
        ))
        # print("main_links:{}".format(main_links))  # for test
        # 根据帖子链接进入详情页爬图片
        sum_img_links = []
        for mlink in main_links:
            UA_HEADER = {
                "User-Agent": "Mozilla/5.0 \
                    (Windows NT 10.0; Win64; x64; rv:66.0) \
                        Gecko/20100101 Firefox/66.0"
            }
            request = urllib.request.Request(mlink, headers=UA_HEADER)
            detail_html = urllib.request.urlopen(request).read().decode()
            detail_xml = etree.HTML(detail_html)
            image_links = list(map(
                lambda x: '<img src="{}">'.format(x),
                detail_xml.xpath('//img[@changedsize="true"]/@src')
            ))
            # print("image_links:{}".format(image_links))  # for test
            sum_img_links.extend(image_links)
        return '\n'.join(sum_img_links)
    return wrapper


@deco_http2xml
def load_page(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 要爬取的地址
        filename: 文件名
        return: html: str
    """

    UA_HEADER = {
        "User-Agent": "Mozilla/5.0 \
            (Windows NT 10.0; Win64; x64; rv:66.0) \
                Gecko/20100101 Firefox/66.0"
    }

    request = urllib.request.Request(url, headers=UA_HEADER)
    response = urllib.request.urlopen(request)

    # print("code: {}\n\n\n url: {}\n\nhtml:{}".format(
    #     response.getcode(), response.geturl(), response.read()))

    ret = response.read().decode("utf-8")
    # print(ret[:3000])
    return ret


def write_page(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print('正在保存{}'.format(filename))

    # UnicodeEncodeError:
    # 'gbk' codec can't encode character '\xba' in position 100787:
    #  illegal multibyte sequence
    # 解决办法，在写入的时候指定编码
    # encoding使用平台默认编码，可以用locale.getpreferredencoding() -> 'cp936' 查看 win的坑
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return True


def tieba_spider(url, begin_page, end_page):
    """
        作用： 贴吧爬虫调度器，负责组合处理每个页面的url
        url： 贴吧url前部分
        begin_page: 起始页
        end_page: 结束页面
    """
    for page in range(begin_page, end_page+1):
        filename = "第" + str(page) + "页.html"
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        # print(fullurl)

        print("正在下载{}".format(filename))
        start = time.time()

        html = load_page(fullurl, filename)
        if write_page(html, filename):
            end = time.time()
            print("{}下载完成,用时{:.2f}秒".format(filename, end-start))
            print("-"*10)


if __name__ == "__main__":
    # keyword = input("请输入要检索的贴吧：")

    # while True:
    #     begin_page = int(input("请输入开始页码："))
    #     end_page = int(input("请输入结束页码："))

    #     if begin_page <= end_page:
    #         break
    #     else:
    #         print("请输入正确的页码范围，如（1，2）")
    keyword = '美女'
    begin_page = 1
    end_page = 1
    kw = {'kw': keyword}
    query = urllib.parse.urlencode(kw)

    url = "https://tieba.baidu.com/f?" + query

    tieba_spider(url, begin_page, end_page)
    print("谢谢使用")
