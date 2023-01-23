#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Mon Jan  9 18:24:27 2023
This code use to save data to databese and create Thread to save data
@author: rafal
'''
import time
import concurrent.futures
#from uart import DataToQueue


class Savedatathread:
    def __init__(self):
        self._running = True
        #self.dataFromUart = DataToQueue()

    def terminate(self):
        self._running = False
        print("thread is ended")

    # Time selection function  Optional 5 sec 15min  and 30min
    def run(self, timer):
        self._running = True
        while self._running:
            if timer == 5:
                '''
                self.t1 = concurrent.futures.ThreadPoolExecutor()
                self.tt1 = self.t1.submit(self.dataFromUart.getDataToQueue)
                self.r = self.tt1.result()
                print(self.r)
                '''

            elif timer == 15:
                print("time t15 is used")
                time.sleep(17)
                print(time.ctime())
            elif timer == 20:
                print("time t20 is used")
                time.sleep(22)
                print(time.ctime())
            else:
                continue
