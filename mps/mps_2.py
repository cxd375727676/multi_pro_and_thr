from multiprocessing import Process, Queue, cpu_count
import os
import time
from numpy.random import random, randint
import pandas as pd

""" 创建多个子进程 """


def write_data(q):
    time.sleep(randint(1, 5))
    print('子进程id: %d， 主进程id: %d' % (os.getpid(), os.getppid()))
    df = pd.DataFrame(random((2, 2)), columns=['x', 'y'])
    q.put(df)


if __name__ == '__main__':
    # multiprocessing.freeze_support()    # 如需打包成exe，需要加上这一句
    # n个核心，n个进程，输出结果全部装入容器， queen是多进程安全的
    print("主进程开始，id: %d" % os.getpid())
    n = cpu_count()
    print("计算机CPU个数: %d" % n)
    q = Queue()    # 队列
    ps = [Process(target=write_data, args=(q,)) for i in range(n)]  # 创建子进程

    for p in ps:
        p.start()
    for p in ps:
        p.join()     # 阻塞主进程
    print("子进程全部结束.")

    while not q.empty():
        print(q.get())
