#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:16
# @Author  : PoLoSec.
# @File    : log.py
# @Software: PyCharm
from datetime import  datetime
import  re
from config import  *
import os
class Log:
    def __init__(self,url,log):
            self.url=url
            self.log=log
            self.filename=self.getname(url)
    def getname(self,url):
        r = re.match(r'http[s]?://([\\\.\w\d:/]+)/', url).group(1)
        r = r.replace(':', '.')
        r = r.replace('/', '.')
        r = r.replace('\\', '.')
        return r + '.txt'

    def save(self):
        print('output at {}'.format(self.filename))
        with open('output/{}'.format(self.filename), 'w+') as f:
            f.write('[TIME] \t\t\t=> {}\n'.format(datetime.now()))
            f.write('[TARGET] \t\t\t=> {}\n'.format(self.url))
            f.write('[NUMBER_OF_THRED] \t=> {}\n'.format(thread))
            f.write('[KEY_WORDS] \t\t=> {}\n'.format(key_words))
            f.write('\n')
            # f.write('{}RESULT{}\n'.format('*'*10, '*'*10))

            for file, status_code in self.log.items():
                f.write('[{}] => {}\n'.format(status_code, file))
        print('\n' + '=' * 30)
        os.system('ls')
        print('=' * 30 + '\n')