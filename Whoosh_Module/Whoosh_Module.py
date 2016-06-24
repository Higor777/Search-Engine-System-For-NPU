#! /usr/bin/env python 
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys,os
import shutil 
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")
from Scrapy_Module.Scrapy_Project.get_sourcedir import get_sourcedir
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
from whoosh.analysis import Tokenizer,Token
from whoosh import scoring
from whoosh import highlight
from jieba.analyse import ChineseAnalyzer 
import logging  
import logging.handlers


class Whoosh_Module(object):
    analyzer = None
    schema = None
    index=None
    indexdir = None
    sourcedir = None
    logfile = None
    logger = None
    indexeddir = None
    def __init__(self):
        file_dir = os.path.split(os.path.realpath(__file__))[0]
        self.logfile = file_dir+'/Whoosh_Module.log'
        self.indexdir = file_dir+'/index/'
        self.sourcedir = get_sourcedir()+'/source/'
        self.indexeddir = get_sourcedir()+'/indexed_source/'
        handler = logging.handlers.RotatingFileHandler(self.logfile, maxBytes = 1024*1024, backupCount = 5) # 实例化handler   
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
        formatter = logging.Formatter(fmt)               # 实例化formatter  
        handler.setFormatter(formatter)                  # 为handler添加formatter  
        self.logger = logging.getLogger('Whoosh_Module') # 获取名为Whoosh_Module的logger  
        self.logger.addHandler(handler)                  # 为logger添加handler  
        self.logger.setLevel(logging.DEBUG)  
        self.logger.info('Whoosh_Module Start.')
        if not os.path.exists(self.sourcedir):
             os.mkdir(self.sourcedir)
        if not os.path.exists(self.indexeddir):
             os.mkdir(self.indexeddir)
        self.analyzer=ChineseAnalyzer()
        self.schema = Schema(title=TEXT(stored=True),path=ID(stored=True),content=TEXT(stored=True,analyzer=self.analyzer))
        if not os.path.exists(self.indexdir):
            os.mkdir(self.indexdir)
            self.index = create_in(self.indexdir,self.schema)
        else :
            self.index = open_dir(self.indexdir)

    def update_index(self):
        file_list = os.listdir(self.sourcedir)
        for sourcefile in file_list:
            try :
                with open(self.sourcedir+sourcefile,'r') as file:
                    url = file.readline().decode('utf-8')
                    tit = file.readline().decode('utf-8')
                    con = file.read().decode('utf-8')
                    if url and tit and con:
                        print url
                        writer = self.index.writer()
                        writer.add_document(title=tit,path=url,content=con)
                        writer.commit()
                        try:
                            shutil.move(self.sourcedir+sourcefile,self.indexeddir+sourcefile)    
                        except:
                            self.logger.info("Move file Error:"+sourcefile)
                    else:
                        continue
            except :
                 self.logger.info("Read file Error:"+sourcefile)
    def run(self):
        while True:
            self.update_index()

    def search(self,keyword,limit=None):
        with self.index.searcher(weighting=scoring.Frequency(),closereader=False) as searcher:
            query = QueryParser("content",self.index.schema).parse(keyword)
            results = searcher.search(query,limit=limit)
            results.highlighter.formatter = highlight.HtmlFormatter(tagname="span", classname="match",termclass='')
            results.order = highlight.SCORE
        return results

    def search_page(self,keyword,page=1,pagelen=10):
        with self.index.searcher(closereader=False) as searcher:
            query = QueryParser("content",self.index.schema).parse(keyword)
            results = searcher.search_page(query,page,pagelen=pagelen)
            print dir(results[0])
            print dir(results)
        return results


if __name__ == '__main__':
    Whoosh = Whoosh_Module()
    Whoosh.run()



