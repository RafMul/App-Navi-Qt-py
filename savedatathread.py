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
import queue
import random
#from uart import sendtempandhumidto_apllication
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Savedatathread:
    def __init__(self):
        self._running = True
        #self.dataFromUart = DataToQueue()
        self.queue_temp = queue.LifoQueue(maxsize=2)
    def terminate(self):
        self._running = False
        logging.info("Thread is ended")


    # Time selection function  Optional 5 sec 15min  and 30min
    def run(self, timer):
        self._running = True
        while self._running:
            if timer == 5:
                self.t1 = concurrent.futures.ThreadPoolExecutor()
                self.tt1 = self.t1.submit(sendtempandhumidto_apllication)
                self.r = self.tt1.result()
                self.queue_temp.put(self.r)
                logging.info("{0:1d}", self.r)


            elif timer == 15:
                logging.info("Time r15 is used")

                time.sleep(17)

            elif timer == 20:
                logging.info("Time T20 is used")
                time.sleep(22)

            else:
                continue

    def returndatatodisplay(self):

        temp = self.queue_temp.get()

        return temp
    def savedata(self):

        while True:
            temp = random.randint(1, 10)
            self.queue_temp.put(temp)
            time.sleep(1)

            '''
                            self.t1 = concurrent.futures.ThreadPoolExecutor()
                            self.tt1 = self.t1.submit(self.dataFromUart.getDataToQueue)
                            self.r = self.tt1.result()
                            print(self.r)
            '''