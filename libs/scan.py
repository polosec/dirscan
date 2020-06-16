#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:16
# @Author  : PoLoSec.
# @File    : scan.py
# @Software: PyCharm
import threading
import user_agent
import  time
import queue
threads=[]
thread_max = threading.BoundedSemaphore(500)
class Scan():

    def __init__(self,url,log,files,req,delay,thread):
        self.url=url
        self.log=log
        self.len,self.req=req
        self.files=files
        self.delay=delay
        self.queue=queue.Queue()
        self.num=0#测试输出
        self.thread=thread
        self.thread_max=threading.BoundedSemaphore(self.thread)
    def realscan(self):
       while not self.queue.empty():
           try:
               filename=self.queue.get()
               url=self.url+filename
               headers = {  # 改变headers头，使该程序更像客户端
                   "User-Agent": "" + user_agent.generate_user_agent() + ""
               }
               response=self.req(url=url,headers=headers)
               self.display(response,filename )
               self.thread_max.release()
           except:
               pass

    def run(self):
        for file in self.files:
                self.queue.put(file)
                self.thread_max.acquire()
                t=threading.Thread(target=self.realscan)
                time.sleep(self.delay)
                threads.append(t)
                t.start()
        for t in threads:
            t.join()
    def display(self,r,file):
        if self.len==-1:
            if r.status_code !=404 and r.status_code !=403:
                print('{}:[{}]=>{}{}'.format(self.num,r.status_code,file,'\t'*5))
                self.log[file]=r.status_code
            else:
                print('{}:[{}]=>{}{}'.format(self.num,r.status_code,file,'\t'*5))
        else:
            if len(r.text)!=self.len:
                print('{}:[{}]=>{}{}'.format(self.num,r.status_code, file, '\t' * 5))
                self.log[file] = r.status_code
            else:
                print('第{}次扫描:[{}] => {}{}'.format(self.num,r.status_code, file, '\t' * 5), end='\r')
        self.num+=1
