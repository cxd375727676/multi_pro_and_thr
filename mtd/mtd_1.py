import threading
import time
""" pycharm \r \b 会将之前的输出抹去 
    
    给主线程任务加一个loading...特效，一旦主线程任务完成，loading特效结束
    
    io密集型，适合多线程"""


def task(a, b):
    time.sleep(10)
    return a + b


def loading(txt, ndots):
    global result
    print(txt, end='', flush=True)
    while not result:
        for _ in range(ndots):
            time.sleep(0.7)
            print('.', end='', flush=True)
        time.sleep(0.7)
        print('\b' * ndots, end='', flush=True)
    print("\n完成任务！")
    print("result = %d" % result)


if __name__ == '__main__':
    result = None
    loading = threading.Thread(target=loading, args=('loading', 3))
    loading.start()
    result = task(1, 2)
