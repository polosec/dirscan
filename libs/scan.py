#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:16
# @Author  : PoLoSec.
# @File    : scan.py
# @Software: PyCharm
import threading
from config import *
import time
class Scan(threading.Thread):

    def __init__(self,url,log,files,req,delay):
        threading.Thread.__init__(self)
        self.url=url
        self.log=log
        self.len,self.req=req
        self.files=files
        self.delay=delay
    def run(self):
        for file in self.files:
            try:
                time.sleep(self.delay)
                r=self.req(self.url+file,timeout=10)
            except:continue
            self.display(r,file)
    def display(self,r,file):
        if self.len==-1:
            if r.status_code !=404 and r.status_code !=403:
                print('[{}]=>{}{}'.format(r.status_code,file,'\t'*5))
                self.log[file]=r.status_code
            else:
                print('[{}]=>{}{}'.format(r.status_code,file,'\t'*5))
        else:
            if len(r.text)!=self.len:
                print('[{}]=>{}{}'.format(r.status_code, file, '\t' * 5))
                self.log[file] = r.status_code
            else:
                print('[{}] => {}{}'.format(r.status_code, file, '\t' * 5), end='\r')


