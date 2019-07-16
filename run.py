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
        self.page = 1
    def loadPage(self, page):
        """
        下载页面
        :return:

        """

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
        gbk_html = html.decode('gbk').encode('utf-8')

        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        content_list = pattern.findall(gbk_html)

        # return content_list
        self.printOnePage(content_list)


    def printOnePage(self, content_list):
        """
            @brief 处理得到的段子列表
            @param item_list 得到的段子列表
            @param page 处理第几页
        """

        for item in content_list:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            self.writePage(item)

    def writePage(self, item):
        """
        写入数据
        :param item:
        :return:
        """
        print "正在写入数据....."
        with open("duanzi.txt", "a") as f:
            f.write(item)

if __name__ == '__main__':

    # 定义一个Spider对象
    spider = Spider()
    spider.loadPage(1)