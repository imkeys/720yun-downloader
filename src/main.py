#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import urllib
import json
import socket
import urllib.request
import urllib.parse
import urllib.error
import time

timeout = 5
socket.setdefaulttimeout(timeout)

class Crawler:
    __time_sleep = 0.1
    __counter = 0
    __dir = './d/'
    __referrer = 'https://www.720yun.com'

    def __init__(self, t=0.1):
        self.time_sleep = t

    def getSuffix(self, name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    def getReferrer(self, url):
        if self.__referrer:
            return self.__referrer
        else:
            par = urllib.parse.urlparse(url)
            if par.scheme:
                return par.scheme + '://' + par.netloc
            else:
                return par.netloc

    def saveImage(self, imgurl):
        if not os.path.exists(self.__dir):
            print('创建文件夹')
            os.mkdir(self.__dir)
        print('开始下载图片')
        time.sleep(self.__time_sleep)
        suffix = self.getSuffix(imgurl)
        # 指定UA和referrer，减少403
        refer = self.getReferrer(imgurl)
        print(refer)
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'),
            ('Referer', refer)
        ]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgurl, self.__dir + str(self.__counter) + str(suffix))

    def start(self):
        imgurl = 'https://ssl-panoimg131.720static.com/resource/prod/b51if9b2281/91b27wfOybf/46844269/imgs/r/l3/05/l3_r_05_03.jpg'
        self.saveImage(imgurl)

if __name__ == '__main__':
	crawler = Crawler(0.05)
	crawler.start()


# https://ssl-panoimg131.720static.com/resource/prod/b51if9b2281/91b27wfOybf/46844269/imgs/r/l3/05/l3_r_05_05.jpg
# https://ssl-panoimg131.720static.com/resource/prod/b51if9b2281/91b27wfOybf/46844269/imgs/r/l3/05/l3_r_05_03.jpg
# https://saas-image.jingwxcx.com/upload_files/2021/11/15/2436c297feb46be565650acdb4d99f2d.jpg
