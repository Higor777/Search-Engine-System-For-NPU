#! /usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.split(os.path.realpath(__file__))[0])
sys.path.append("../")
from Whoosh_Module.Whoosh_Module import Whoosh_Module
from Scrapy_Module.Scrapy_Project.spiders.statistics.statistics import statistics
from flask import Flask,url_for,render_template,request

Whoosh = None
Statis = None
flask_app = Flask(__name__)
@flask_app.route('/',methods=['GET', 'POST'])
def index():
    global Whoosh
    if request.method == 'GET':
        #keyword=request.form['keyword']
        keyword=request.args.get('kw')
        page=request.args.get('pg')
        if page:
            page=int(page)
        else:
            page=1
        if(page<=0):
            page=1
        if keyword:
            results = Whoosh.search(keyword)
            pagenum = int(results.scored_length()/10)+1
            #results = Whoosh.search_page(keyword,page=page,pagelen=10)
            return render_template('result.html',results=results,keyword=keyword,page=page,pagenum=pagenum)
        else :
            return render_template('index.html',results=None)
    else :
        return render_template('index.html',results=None)

@flask_app.route('/statistics/',methods=['GET', 'POST'])
def statis():
    global Statis
    Statis = statistics()
    return render_template('statistics.html',statistics=Statis)


class Flask_Module(object):
    def __init__(self,WhooshName):
        global Whoosh
        Whoosh = WhooshName
    def run(self):
        #flask_app.debug=True
        flask_app.run(host='0.0.0.0',port=5000)

if __name__ == '__main__':
    Whoosh=Whoosh_Module()
    #flask_app.debug=True
    flask_app.run(host='0.0.0.0')

