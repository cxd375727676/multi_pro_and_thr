from multiprocessing import Pool, Manager, cpu_count, Process
import os
from numpy.random import random
import time
import pandas as pd

""" 创建多个子进程，大于cpu核心数
    一旦进程池满，则会等某个子进程结束再开始新的进程
    
    创建一个实时读取数据的子进程"""


def write_data(q, i):
    time.sleep(i)
    print('子进程%d id: %d， 主进程id: %d' % (i, os.getpid(), os.getppid()))
    df = pd.DataFrame(random((2, 2)), columns=['x', 'y'])
    q.put(df)
    print('子进程%d结束' % i)


def read_data(q):
    while True:
        data = q.get()
        print("get data:", data)


if __name__ == '__main__':
    # multiprocessing.freeze_support()    # 如需打包成exe，需要加上这一句
    # n个核心，n个进程，输出结果全部装入容器， queen是多进程安全的
    print("主进程开始，id: %d" % os.getpid())
    print("计算机CPU个数: %d" % cpu_count())
    q = Manager().Queue()
    p = Pool()    # 默认cpu核心数

    m = 7    # 创建7个写数据进程
    for i in range(m):
        p.apply_async(write_data, (q, i))
    p.close()
    rp = Process(target=read_data, args=(q,))   # 读进程
    rp.start()
    p.join()
    print("读数据子进程全部结束.")
    rp.terminate()   # 终止读进程，因为是死循环
    print("子进程全部结束")
