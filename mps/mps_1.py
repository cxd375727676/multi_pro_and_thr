from multiprocessing import Pool, Manager, cpu_count
import os
from numpy.random import random
import time
import pandas as pd


"""多进程并行，汇总结果给主进程
   使用了进程池Pool"""


def write_data(q, i):
    time.sleep(i)
    print('子进程%d id: %d， 主进程id: %d' % (i, os.getpid(), os.getppid()))
    df = pd.DataFrame(random((2, 2)), columns=['x', 'y'])
    q.put(df)


if __name__ == '__main__':
    # multiprocessing.freeze_support()    # 如需打包成exe，需要加上这一句
    # n个核心，n个进程，输出结果全部装入容器， queen是多进程安全的
    print("主进程开始，id: %d" % os.getpid())
    n = cpu_count()
    print("计算机CPU个数: %d" % n)
    q = Manager().Queue()
    p = Pool(n)
    for i in range(n):
        p.apply_async(write_data, (q, i))
    p.close()
    p.join()
    print("子进程全部结束.")

    while not q.empty():
        print(q.get())
