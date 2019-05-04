import scrapy
from mySpider.items import ItcastItem
import locale


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名，启动爬虫时使用的，scrapy crawl itcast
    # 网站域名，允许爬取的范围
    allowed_domains = ["http://www.itcast.cn/"]
    # 从那个网址开始爬取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        """
        处理响应内容
        """
        # for test
        # 注意 wb 以二进制方式写入！！
        # with open('itcast.html', 'wb') as fw:
        #     fw.write(response.body)

        teacher_info = []
        teacher_list = response.xpath('//div[@class="li_txt"]')
        for teacher in  teacher_list:

            name = teacher.xpath('./h3/text()').extract()  # 提取所有list()， extract_first 提取第一个str
            title = teacher.xpath('./h4/text()').extract()
            info = teacher.xpath('./p/text()').extract()

            item = ItcastItem()
            # for json Unicode 编码 全平台通用
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # for csv
            # cur_code = locale.getpreferredencoding(False)  # 获取当前用户可能使用的编码 'UTF-8'
            # item['name'] = name[0].encode(cur_code)
            # item['title'] = title[0].encode(cur_code)
            # item['info'] = info[0].encode(cur_code)

            teacher_info.append(item)

        return teacher_info
        # 返回到外面 可以通过 scrapy crawl itcast -o <filename>
        # filename 可以为 .json .csv 等
        # 输出.json 为Unicode www.json.cn 可以看到转换后的结果
        # csv 可以通过 Excel 打开
