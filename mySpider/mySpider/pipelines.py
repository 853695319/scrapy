# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json


class ItcastPipeline(object):
    def __init__(self):
        """
        可选方法：
        初始化一个file-like object
        """
        self.f = open('tea.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        """
        必须存在的方法
        """
        json_txt = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(json_txt)
        return item

    def close_spider(self, spider):
        """
        可选方法：
        爬虫结束时调用这方法
        """
        self.f.close()
        print("\n\n-------文件关闭----------\n\n")
