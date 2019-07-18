"""
sem.py  信号量演示
思路: 信号量数量相当与资源，执行任务必须消耗资源
"""

from multiprocessing import Process,Semaphore
from time import sleep
import os

# 创建信号量 (最多允许3个任务同时执行)
sem = Semaphore(3)

# 任务函数
def handle():
    sem.acquire() # 想执行必须消耗一个信号量
    print("%s 执行任务"%os.getpid())
    sleep(2)
    print("%s 执行任务完毕"%os.getpid())
    sem.release() # 归还信号量

# 10个任务需要执行
for i in range(10):
    p = Process(target = handle)
    p.start()
