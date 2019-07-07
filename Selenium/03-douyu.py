#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


class TestDouyu(unittest.TestCase):
    def setUp(self):
        # 初始化方法
        self.driver = webdriver.PhantomJS(executable_path=r'L:\code\scrapy\Selenium\phantomjs.exe')
        pass

    def testDouyu(self):
        self.driver.get('https://www.douyu.com/directory/all')
        while True:
            # 通过解析源码来获得数据，不同的角度,这样做的目的就是为了遍历网页
            # 因为过去用HttpClient获取动态页面是没有加载到动态数据的，所以要用浏览器
            markup = self.driver.page_source
            soup = BeautifulSoup(markup, "html.parser")  # 其实应该用lxml，但是我目前没安装，所以用Python标准库
            room_name_list = soup.find_all('h3', attrs={'class': 'DyListCover-intro'})
            room_viewer_list = soup.find_all('span', attrs={'class': 'DyListCover-hot'})

            for room_name, room_viewer in zip(room_name_list, room_viewer_list):
                print('room_name: {}, room_viewer:{}'.format(room_name.get_text().strip(), room_viewer.get_text().strip()))
            if self.driver.page_source.find('dy-Pagination-disabled dy-Pagination-next') != -1:
                break

            self.driver.find_element_by_class_name('dy-Pagination-next').click()
            print('Next Page')
        pass

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
