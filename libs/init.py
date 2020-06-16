#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 9:39
# @Author  : PoLoSec.
# @File    : init.py
# @Software: PyCharm\
from config import *
import  requests
from libs.scan import  Scan
from libs.log import Log
class Init():
    def __init__(self,args):
        self.url=self.init_url(str(args.url))
        self.keywords=args.keywords
        self.delay=args.delay
        self.method=args.method
        if args.thread!="":

            self.thread=int(args.thread)
        else:
            self.thread=thread
    def help(self):
            help = 'Useage : python ctf-wscan.py url [-k means keywordlist] [-t means thread num] [-m means method 0=head 1=get] [-d means delay]\n'
            help += 'Example: python ctf-wscan.py http://ctf.test.com   -k keyword1,keyword2 -t 10 -m 1 -d 0.5'
            print(help)
            exit()
    def init_url(self,url):
        if not url.startswith('http'):
            url='http://'+url
        if not url.endswith('/'):
            url=url+'/'
        return url
    def start(self):
        loglist={}
        files=self.getfiles()
        req=self.detect()
        scan=Scan(self.url,loglist,files,req,self.delay,self.thread)
        scan.run()
        if enable_log:
            log=Log(self.url,loglist)
            log.save(self.method,self.delay,self.thread)
    def getfiles(self):
        with open('dict/dict.txt') as f:
            files=f.readlines()
        if self.keywords:
            g=GenerateDict(self.keywords)
            for i in g.generate():
                files.append(i)
        files=(file.strip() for file in files)
        return files
    def detect(self):
        import uuid,random,string
        rand1=''.join(random.sample(string.ascii_letters,8))
        rand2=uuid.uuid4()
        rand3=random.randint(10000,9999999)
        req=requests.get
        r1=requests.get(self.url+str(rand1))
        r2 = requests.get(self.url + str(rand2))
        r3 = requests.get(self.url + str(rand3))
        code = int(self.method) if self.method != "" else int(method)

        if r1.status_code==r2.status_code==r3.status_code ==200 and len(r1.text)==len(r2.text)==len(r3.text):
            code=3
            req=requests.get
            return  len(r1.text),req #代表的是404页面的长度
        else:
            if code==1:
                req=requests.head
            elif code==2:
                req=requests.get
            return -1,req
class GenerateDict():
    def __init__(self,keywords):
        self.keywords=[]
        self.exts=self.getexts()
        if keywords:
            self.keywords+=keywords
            key_words.extend(self.keywords)
        elif key_words:
            self.keywords+=key_words
        else: pass
    def getexts(self):
        with open('dict/ext.txt') as f:
            exts=f.readlines()
            return [ext.strip() for ext in exts]
    def generate(self):
        for e in self.exts:
            for kw in self.keywords:
                yield e.replace('$',kw)


