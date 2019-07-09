# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dgsun.items import DgsunItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    start_urls = [f'http://wz.sun0769.com/index.php/question/questionType?type=4&page={offset}']

    rules = (
        # self.follow = False if callback else True
        # 也就是默认有callback就不follow,没callback就follow

        # 页码
        Rule(
            LinkExtractor(allow=r'type=4&page=\d*'),
            follow=True  # follow=True,那么爬取到符合规则的URL，就会不断抽取URL,可以爬取全部分页
            # follow=False # 只抽取当前页面一次，不follow抽取的URL，只是当前页
        ),

        # 处理帖子内容
        Rule(
            LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),
            callback='parse_item',
            follow=False
        ),
    )

    def parse_item(self, response):
        try:
            item = DgsunItem()
            # 标题
            item['title'] = response.css('div.wzy1 span.niae2_top::text').get()

            # 编号
            item['number'] = response.css('div.wzy1 span:nth-child(2)::text').get().split(':')[-1]

            # 文字内容，默认先取出有图片情况下的文字内容列表
            item['content'] = response.css('div.wzy1 .txt16_3 *::text').get().strip()

            # 链接
            item['url'] = response.url

            yield item
        except Exception as err:
            self.logger.exception('')
