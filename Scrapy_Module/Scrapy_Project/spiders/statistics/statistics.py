# -*- coding: utf-8 -*-
import os
class statistics(object):
    status_num = {'301':0,'302':0,'400':0,'403':0,'404':0,'500':0,'503':0,'504':0}
    file_301num = ''
    file_302num = ''
    file_403num = ''
    file_400num = ''
    file_404num = ''
    file_500num = ''
    file_503num = ''
    file_301list = ''
    file_302list = ''
    file_403list = ''
    file_400list = ''
    file_404list = ''
    file_500list = ''
    file_503list = ''
    file_504list = ''
    list_301 = []
    list_302 = []
    list_400 = []
    list_403 = []
    list_404 = []
    list_500 = []
    list_503 = []
    list_504 = []
    def __init__(self):
        file_dir = os.path.split(os.path.realpath(__file__))[0]
        self.file_301num = file_dir + '/301num'
        self.file_302num = file_dir + '/302num'
        self.file_400num = file_dir + '/400num'
        self.file_403num = file_dir + '/403num'
        self.file_404num = file_dir + '/404num'
        self.file_500num = file_dir + '/500num'
        self.file_503num = file_dir + '/503num'
        self.file_504num = file_dir + '/504num'
        self.file_301list = file_dir + '/301list'
        self.file_302list = file_dir + '/302list'
        self.file_400list = file_dir + '/400list'
        self.file_403list = file_dir + '/403list'
        self.file_404list = file_dir + '/404list'
        self.file_500list = file_dir + '/500list'
        self.file_503list = file_dir + '/503list'
        self.file_504list = file_dir + '/504list'
        if os.path.isfile(self.file_301num):
            file = open(self.file_301num,'r')
            self.status_num['301'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_301num,'w')
            file.write(str(self.status_num['301']))
            file.close()
        if os.path.isfile(self.file_302num):
            file = open(self.file_302num,'r')
            self.status_num['302'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_302num,'w')
            file.write(str(self.status_num['302']))
            file.close()
        if os.path.isfile(self.file_400num):
            file = open(self.file_400num,'r')
            self.status_num['400'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_400num,'w')
            file.write(str(self.status_num['400']))
            file.close()
        if os.path.isfile(self.file_403num):
            file = open(self.file_403num,'r')
            self.status_num['403'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_403num,'w')
            file.write(str(self.status_num['403']))
            file.close()
        if os.path.isfile(self.file_404num):
            file = open(self.file_404num,'r')
            self.status_num['404'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_404num,'w')
            file.write(str(self.status_num['404']))
            file.close()
        if os.path.isfile(self.file_500num):
            file = open(self.file_500num,'r')
            self.status_num['500'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_500num,'w')
            file.write(str(self.status_num['500']))
            file.close()
        if os.path.isfile(self.file_503num):
            file = open(self.file_503num,'r')
            self.status_num['503'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_503num,'w')
            file.write(str(self.status_num['503']))
            file.close()
        if os.path.isfile(self.file_504num):
            file = open(self.file_504num,'r')
            self.status_num['504'] = int(file.readline())
            file.close()
        else:
            file = open(self.file_504num,'w')
            file.write(str(self.status_num['504']))
            file.close()
        file = open(self.file_301list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_301.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_302list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_302.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_400list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_400.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_403list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_403.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_404list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_404.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_500list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_500.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_503list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_503.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
        file = open(self.file_504list,'a+')
        line = file.readline().strip().lstrip().rstrip('\n')
        while line:
            self.list_504.append(line)
            line = file.readline().strip().lstrip().rstrip('\n')
        file.close()
    def record(self,response):
        status = response.status
        url = response.url
        #print type(status),status
        #print url
        if url in self.list_301 or url in self.list_302 or url in self.list_400 or url in self.list_403 or url in self.list_404 or url in self.list_500 or url in self.list_503 or url in self.list_504:
            print 'Url already exists.'
            return
        if status == 301:
            self.status_num['301']=self.status_num['301']+1
            file = open(self.file_301num,'w')
            file.write(str(self.status_num['301']))
            file.close()
            file = open(self.file_301list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 302:
            self.status_num['302']=self.status_num['302']+1
            file = open(self.file_302num,'w')
            file.write(str(self.status_num['302']))
            file.close()
            file = open(self.file_302list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 400:
            self.status_num['400']=self.status_num['400']+1
            file = open(self.file_400num,'w')
            file.write(str(self.status_num['400']))
            file.close()
            file = open(self.file_400list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 403:
            self.status_num['403']=self.status_num['403']+1
            file = open(self.file_403num,'w')
            file.write(str(self.status_num['403']))
            file.close()
            file = open(self.file_403list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 404:
            self.status_num['404']=self.status_num['404']+1
            file = open(self.file_404num,'w')
            file.write(str(self.status_num['404']))
            file.close()
            file = open(self.file_404list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 500:
            self.status_num['500']=self.status_num['500']+1
            file = open(self.file_500num,'w')
            file.write(str(self.status_num['500']))
            file.close()
            file = open(self.file_500list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 503:
            self.status_num['503']=self.status_num['503']+1
            file = open(self.file_503num,'w')
            file.write(str(self.status_num['503']))
            file.close()
            file = open(self.file_503list,'a+')
            file.write(url+'\n')
            file.close()
        elif status == 504:
            self.status_num['504']=self.status_num['504']+1
            file = open(self.file_504num,'w')
            file.write(str(self.status_num['504']))
            file.close()
            file = open(self.file_504list,'a+')
            file.write(url+'\n')
            file.close()
        else:
            print 'Status ',status,' not in the list.'
            
