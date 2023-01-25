#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:48:16 2022

@author: rafal
"""

import serial
import time
import queue
import logging
import random


logging.basicConfig(level=logging.INFO, format='%(message)s')

"""Save data from uart to queue"""
__initidata = True


class DataSaveToQueue:
    def __init__(self):
        """ Create queue format LIFO"""
        self.queue_temp = queue.LifoQueue(maxsize=5)
        self.queue_humid = queue.LifoQueue(maxsize=4)
        self.queue_hour = queue.LifoQueue(maxsize=2)
        self.queue_minute = queue.LifoQueue(maxsize=2)
        self.queue_second = queue.LifoQueue(maxsize=2)
        self.queue_satelitenumber = queue.LifoQueue(maxsize=2)

    def getDataToQueue(self):  # Generator data
        logging.info("Run save data to queue")

        while True:
            try:

                stm32 = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)
                time.sleep(0.1)
            except:
                logging.info("No connection with STM32")

                break

            try:
                stm32.inWaiting() == 0
            except:
                logging.info("No data")
                time.sleep(0.4)
                continue
            '''
        while stm32.inWaiting() == 0:

            pass
            '''
            data = stm32.readline()
            data = str(data, 'utf-8')
            data = (data.strip('\n\r'))
            splitdata = data.split(',')

            temp = float(splitdata[3])

            humid = float(splitdata[4])
            hour = (splitdata[0])
            minute = (splitdata[1])
            second = (splitdata[2])
            satelitenumber = (splitdata[5])
            self.queue_temp.put(temp)
            self.queue_humid.put(humid)
            self.queue_hour.put(hour)
            self.queue_minute.put(minute)
            self.queue_second.put(second)
            self.queue_satelitenumber.put(satelitenumber)
            logging.info("Currently selected index - {0:1d}", splitdata)
              # self.queue.put(None)

    def addDatatoqueue(self):  # Consumer number one
        while True:
            s = self.queue_temp.get()

            pass

    def sendtempandhumidto_apllication(self):  # Consumer number two
        while self.queue_temp.empty():

            # dopisać kolejki do kolejnych danych i funkcje je odbierające

            temp = self.queue_temp.get()
            self.queue_temp.task_done()
            return temp

    def senddatatosisplay(self):  # Consumer number three

        temp = self.queue_temp.get()

        self.queue_temp.task_done()
        return temp
    def savedata(self):     #Producer

        while True:
            while (self.queue_temp.full())and(self.queue_humid.full()):
                print('queue is full')
                break
            temp = random.randint(1, 10)
            self.queue_temp.put(temp)
            self.queue_humid.put(temp)
            print(temp)



    '''
          stm32 = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)
          time.sleep(0.1)
          while(stm32.inWaiting()==0):
                
                logging.info("Currently selected index - {0:1d}", self.onTheTopIndex)
                pass
        
          data = stm32.readline()
          data = str(data, 'utf-8')
          data = (data.strip('\n\r'))
          
          splitdata=data.split(',')

          
          self.temp = float(splitdata[3])
          self.humid = float(splitdata[4])
          self.hour = (splitdata[0])
          self.minute = (splitdata[1])
          self.second = (splitdata[2])
          #self.satelitenumber= (splitdata[5] )
          
          
          
        #print ('{0:2s}:{1:2s}:{2:2s}'.format(self.hour,self.minute,self.second),"temp = ",self.temp, "humid = ", self.humid,"satelita number",self.satelitenumber)
          
          return (splitdata)
        
'''
