#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'

'''
用urllib.request.urlretrieve()函数和多线程来下载这些电子书
'''
import time
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
from urllib import request
import os


# request.urlretrieve() 下载电子书文件
def download(url):
    #书名
    book_name = os.path.join(os.path.curdir,'Ebooks\\') + url.split('/')[-1]
    print("正在下载的电子书是: %s" % book_name) # 开始下载
    request.urlretrieve(url,book_name)
    print('%s 电子书下载完成' % book_name) # 完成下载

def main():
    start_time = time.time() # 开始时间

    file_path = os.path.join(os.path.curdir,'Ebooks\\ebooks.txt') # txt文件路径

    # 读取txt文件内容,即电子书的链接
    with open(file_path,'r') as f:
        urls = f.readlines()

    urls = [__.strip() for __ in urls]


    # 利用python的多线程进行电子书下载
    # 多线程完成后，进入后面的操作
    # wait方法接收3个参数，等待的任务序列、超时时间以及等待条件。等待条件return_when默认为ALL_COMPLETED，表明要等待所有的任务都结束。
    # 可以看到运行结果中，确实是所有任务都完成了,主线程才打印出 “下载完成用时多长”。
    # 等待条件还可以设置为FIRST_COMPLETED，表示第一个任务完成就停止等待

    executor = ThreadPoolExecutor(len(urls))
    future_tasks = [executor.submit(download,url) for url in urls]
    wait(future_tasks,return_when=ALL_COMPLETED)

    # 统计所用时间
    end_time = time.time()
    print('共计 %s 完成下载' % (end_time - start_time))


if __name__ == "__main__":
    main()


















