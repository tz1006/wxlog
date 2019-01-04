
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# filename: filelog.py
# version: 0.0.1
# description: filelog
# useage: from filelog import 


from prettytable import PrettyTable
from datetime import datetime
from pytz import timezone
from concurrent.futures import ThreadPoolExecutor
import os
import queue




class log():
    def __init__(self, path):
        self.wechat = wechat
        self.path = path
        self.checkdir(path)
        self.queue = queue.Queue()
        self.start()
    def checkdir(self, path):
        dirfile = path.rsplit('/', 1)
        if len(dirfile) == 2:
            dir = dirfile[0]
            if os.path.exists(dir) == False:
                os.makedirs(dir)
                print('初始化 %s' % path)
    def write(self, message, level='INFO', show=0):
        time = datetime.now(timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")
        text = '{} [{}] - {}'.format(time, level, message)
        self.queue.put(text)
        if show != 0:
            print(text)
    def writer(self):
        while self.logging == True:
            text = self.queue.get()
            with open(self.path , 'a') as f:
                f.write(text + '\n')
    def start(self):
        self.queue.queue.clear()
        self.logging = True
        pool = ThreadPoolExecutor(max_workers=1)
        pool.submit(self.writer)
    def exit(self):
        self.logging = False
        self.write('Log 退出.')




def read(path, line=15):
    table = PrettyTable(["TIME", "LEVEL", "MESSAGE"])
    with open(path) as f:
        txt = f.readlines()
    if len(txt) < line:
        line = len(txt)
    for i in range(line):
        i = - (i + 1)
        text = txt[i].replace('\n', '')
        time = text.rsplit(' ',3)[0]
        level = text.split('[')[1].split(']')[0]
        message = text.rsplit(' ',1)
        table.add_row([time, level, message])
    print(table)




if __name__ == '__main__':
    import code
    code.interact(banner = "", local = locals())


# a = log('test.log')
# a.exit()
# a.write('This is the first log.')
