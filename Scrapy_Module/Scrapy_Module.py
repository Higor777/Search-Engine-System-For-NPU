#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.split(os.path.realpath(__file__))[0])
from Scrapy_Project.spiders.Scrapy_ModuleSpider import Scrapy_ModuleSpider
# scrapy api
from scrapy import signals
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import  scrapy.utils.project as Scr_pro
import logging  
import logging.handlers

class Scrapy_Module(object):
    Scrapy_Module_setting = None
    logfile = 'Scrapy_Module.log'
    def __init__(self):
        #记录当前工作用于还原工作目录
        cwd = os.getcwd()
        #获取当前文件所在目录，并把工作目录切换到文件所在目录，用于读取Scrapy项目settings
        file_dir = os.path.split(os.path.realpath(__file__))[0]
        os.chdir(file_dir)
        self.Scrapy_Module_setting = Scr_pro.get_project_settings()
        #关闭打印信息
        self.Scrapy_Module_setting.set('LOG_ENABLED',False)
        handler = logging.handlers.RotatingFileHandler(self.logfile, maxBytes = 1024*1024, backupCount = 5) # 实例化handler   
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
        formatter = logging.Formatter(fmt)               # 实例化formatter  
        handler.setFormatter(formatter)                  # 为handler添加formatter 
        self.logger = logging.getLogger('Scrapy_Module') # 获取名为Scrapy_Module的logger  
        self.logger.addHandler(handler)                  # 为logger添加handler  
        self.logger.setLevel(logging.DEBUG)  
        self.logger.info('Scrapy_Module Start.')
        #将工作目录还原为之前的工作目录
        os.chdir(cwd)
    def spider_closing(self,spider):
        #收到Spider结束信号后关闭reactor
        self.logger.info("Closing reactor")
        reactor.stop()
    def crawl(self):
        spider = Scrapy_ModuleSpider()
        Runner = CrawlerRunner(self.Scrapy_Module_setting)
        cra = Runner.crawl(spider)
        # stop reactor when spider closes
        cra.addBoth(lambda _: self.spider_closing(cra))
        self.logger.info("Run reactor")
        reactor.run()
    def run(self):
        while True:
            self.crawl()


if __name__ == '__main__' :
    Scrapy_Module().run()
