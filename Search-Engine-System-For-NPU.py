#! /usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from Scrapy_Module.Scrapy_Module import Scrapy_Module
from Whoosh_Module.Whoosh_Module import Whoosh_Module
from Flask_Module.Flask_Module import Flask_Module

__author__ = "Higor"
__team__ = "Team of IS"
__version__ = "v1.1"

class Search_Engine_System_For_NPU(object):
    def __init__(self):
        self.Scrapy = Scrapy_Module()
        self.Whoosh = Whoosh_Module()
        self.Flask = Flask_Module(self.Whoosh)
        self.Flasktask = threading.Thread(target=self.Flask.run)
        self.Whooshtask = threading.Thread(target=self.Whoosh.run)
    def run(self):
        self.Flasktask.start()
        self.Whooshtask.start()
        self.Scrapy.run()
        self.Flasktask.join()
        self.Whooshtask.join()

if __name__ == '__main__':
     Search_Engine_System_For_NPU().run()

