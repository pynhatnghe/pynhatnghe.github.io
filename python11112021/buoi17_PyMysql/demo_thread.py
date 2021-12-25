import time
import threading
import math
from multiprocessing import Process, process
import os


def Hello(name):
    print(f"Hello {name}")


def Calculate(a, b):
    result = math.pow(a, b) / (a + b)
    print(f"{a} **** {b} = {result}")


# Demo sync : gọi đồng bộ theo thứ tự
time_start = time.time()
Hello('PyNhatNghe')
Calculate(11, 99.99)
time_stop = time.time()
print("Tổng thời gian chạy:", time_stop - time_start)


# Demo async: gọi bất đồng bộ
time_start = time.time()
threadLock = threading.Lock()
threads = []
thread1 = threading.Thread(target=Hello, args=('PyNhatNghe', ))
thread2 = threading.Thread(target=Calculate, args=(11, 99.99))
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

# CHờ đợi tất cả đều hoàn thành
for item in threads:
    item.join()

time_stop = time.time()
print("Tổng thời gian chạy:", time_stop - time_start)


# Demo multi process
time_start = time.time()
processes = []
process1 = Process(target=Hello, args=('PyNhatNghe', ))
process2 = Process(target=Calculate, args=(11, 99.99))
process1.start()
process2.start()
processes.append(process1)
processes.append(process2)

# CHờ đợi tất cả đều hoàn thành
for item in processes:
    item.join()

time_stop = time.time()
print("Tổng thời gian chạy:", time_stop - time_start)
