from multiprocessing import Process
import time
"""观察主进程与子进程的关系"""


# 子进程
def f(seconds):
    print("子进程开始")
    time.sleep(seconds)
    print("子进程结束")
# ==================================================
# 1. 什么都不限制


# if __name__ == '__main__':
#     print("主进程开始")
#     p = Process(target=f, args=(7,))
#     p.start()
#     time.sleep(5)
#     print("主进程结束")
# 结论: 所有进程（主、子）执行完毕后程序退出

# ======================================================
# 2. 阻塞主进程，等待子进程结束


# if __name__ == '__main__':
#     print("主进程开始")
#     p = Process(target=f, args=(7,))
#     p.start()
#     p.join()
#     time.sleep(5)
#     print("主进程结束")

# =====================================================
# 3. 设置子进程为守护进程，主进程结束后子进程也结束
if __name__ == '__main__':
    print("主进程开始")
    p = Process(target=f, args=(7,), daemon=True)
    p.start()
    time.sleep(5)
    print("主进程结束")
