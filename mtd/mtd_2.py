import threading
import time
"""观察主线程与子线程的关系"""


# 子线程
def f(seconds):
    print("子线程开始")
    time.sleep(seconds)
    print("子线程结束")
# ==================================================
# 1. 什么都不限制


# if __name__ == '__main__':
#     print("主线程开始")
#     th = threading.Thread(target=f, args=(7,))
#     th.start()
#     time.sleep(5)
#     print("主线程结束")
# 结论: 所有线程（主、子）执行完毕后程序退出（python解释器进程结束）

# ======================================================
# 2. 阻塞主线程，等待子线程结束


# if __name__ == '__main__':
#     print("主线程开始")
#     th = threading.Thread(target=f, args=(7,))
#     th.start()
#     th.join()
#     time.sleep(5)
#     print("主线程结束")

# =====================================================
# 3. 设置子线程为守护线程，主线程结束后子线程也结束
if __name__ == '__main__':
    print("主线程开始")
    th = threading.Thread(target=f, args=(7,), daemon=True)
    th.start()
    time.sleep(5)
    print("主线程结束")
