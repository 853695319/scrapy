from queue import Queue
import threading
import json
from lxml import etree
import requests


class SpiderWorker(threading.Thread):
    def __init__(self, name, page_queue, parse_queue):
        super(SpiderWorker, self).__init__(name=name)
        self.page_queue = page_queue
        self.parse_queue = parse_queue

    def run(self):
        while True:
            page = self.page_queue.get()
            if page is None:
                break

            print("{}爬取页码-{}-开始".format(self.name, page))
            html = self.spider_qiushi(page)
            print("{}爬取页码-{}-完成".format(self.name, page))

            # 将爬取的HTML源码放入处理队列
            self.parse_queue.put((html, page))
            # 本次任务完成
            self.page_queue.task_done()

    @staticmethod
    def spider_qiushi(page):
        """
        :param page: 指定爬取页码
        :return html: 返回爬取的html（string）
        """
        url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
        ua_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
        response = requests.get(url, headers=ua_header)
        print("status_code:%d" % response.status_code)
        html = response.text
        return html


class ParseWorker(threading.Thread):
    def __init__(self, name, data_queue):
        super(ParseWorker, self).__init__(name=name)
        self.q = data_queue

    def run(self) -> None:
        while True:
            item = self.q.get()
            if item is None:
                break
            html, page = item
            print("{}处理页码-{}-开始".format(self.name, page))
            self.parse_html(html)
            print("{}处理页码-{}-结束".format(self.name, page))
            # 本次任务完成
            self.q.task_done()

    @staticmethod
    def parse_html(html):
        xml = etree.HTML(html)
        article_box = xml.xpath('//div[contains(@id, "qiushi_tag_")]')
        for article in article_box:
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


class MyThreadQueue:
    def __init__(self, get_queue, thread_num, worker, my_source, other_q=None):
        self.q = get_queue  # 线程取任务队列
        self.num_worker_threads = thread_num  # 开启线程数
        self.worker = worker  # 线程实例
        self.source = my_source  # 爬取范围
        self.other_q = other_q  # 默认单队列
        self.threads = []

    def start_work(self):
        # 开启页面爬虫
        threads_name = ['线程{}号'.format(i) for i in range(self.num_worker_threads)]
        if self.other_q is None:
            for i in range(self.num_worker_threads):
                t = self.worker(threads_name[i], self.q)
                t.start()
                self.threads.append(t)
        else:
            for i in range(self.num_worker_threads):
                t = self.worker(threads_name[i], self.q, self.other_q)
                t.start()
                self.threads.append(t)

        for item in self.source():
            self.q.put(item)

    def join_work(self):
        # block until all tasks are done
        # 堵塞直到队列为空，且爬虫全部结束任务
        self.q.join()
        # stop workers
        for i in range(self.num_worker_threads):
            self.q.put(None)
        for t in self.threads:
            t.join()


def source():
    return range(1, 7)


def main():
    page_queue = Queue(3)  # 页码队列
    data_queue = Queue(3)  # 解析HTML队列

    spider_page = MyThreadQueue(page_queue, 3, SpiderWorker, source, data_queue)
    parse_html = MyThreadQueue(data_queue, 3, ParseWorker, source)

    spider_page.start_work()
    parse_html.start_work()

    spider_page.join_work()
    parse_html.join_work()
