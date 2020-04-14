from threading import Thread
import threading
import os

class thread_class(threading.Thread):
    def __init__(self,num):
        threading.Thread._init_(self)
        self.num = num

    def run(self):
        for i in num:
            print(i)

            
thread1 = thread_class(10)
thread2 = thread_class(20)
thread1.start()
thread2.start()