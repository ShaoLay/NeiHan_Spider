#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Hamdi
import urllib2
import re


class Spider:
    """
    内涵段子爬虫类
    """
    def __init__(self):
        """
        初始化
        """
        self.page = 1

    def loadPage(self, page):
        """
        下载页面
        :return:

        """

        print '正在下载数据……'
        url = "https://www.neihan8s.com/article/list_5_" + str(page) + ".html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        # 请求页面
        request = urllib2.Request(url, headers=headers)
        # 打开页面
        response = urllib2.urlopen(request)
        # 读取页面, 返回给html
        html = response.read()
        html = html.decode('gbk').encode('utf-8')
        print html


if __name__ == '__main__':

    # 定义一个Spider对象
    spider = Spider()
    spider.loadPage(1)