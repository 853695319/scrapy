#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys， 可以使用操作键盘、标签和鼠标
from selenium.webdriver.common.keys import Keys

# options = webdriver.FirefoxOptions()
# options.headless = True
# firefox = webdriver.Firefox(executable_path=r'L:\code\scrapy\Selenium\geckodriver.exe', options=options)
# url = 'https://bbs.level-plus.net/'
# firefox.get(url)
driver = webdriver.PhantomJS(executable_path=r"L:\code\scrapy\Selenium\phantomjs.exe")
driver.get('https://bbs.level-plus.net/')
driver.save_screenshot('soul_plus.png')  # 能截取整个网页，比Firefox好

# login before
driver.find_element_by_name('pwuser').send_keys('xxx')
driver.find_element_by_name('pwpwd').send_keys('xxx')
driver.save_screenshot('login_before.png')

# login after
driver.find_element_by_class_name('btn').click()
driver.save_screenshot('login_after.png')
