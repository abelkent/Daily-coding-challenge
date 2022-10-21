# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:26:33 2022

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

@author: abelw
"""
import threading
import time
import datetime

#Use time.sleep()
def scheduler(f, n):
    time.sleep(n / 1000)
    f()

#Use threading.Timer
def scheduler_2(f,n):
    threading.Timer(n/1000, f).start()


#Test function to be triggered after delay
def test():
    print("Hello!")


scheduler(test, 1000)
print("Wee")