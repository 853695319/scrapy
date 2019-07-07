# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DgsunPipeline(object):
    def __init__(self):
        # 创建一个只写文件，指定文本编码格式为utf-8
        self.file = open('sunwz.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        json_txt = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(json_txt)
        return item

    def spider_closed(self, spider):
        self.file.close()
