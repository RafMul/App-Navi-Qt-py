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

logging.basicConfig(level=logging.INFO, format='%(message)s')

""" Create queue format LIFO"""

queue_temp = queue.LifoQueue(maxsize=2)
queue_humid = queue.LifoQueue(maxsize=2)
queue_hour = queue.LifoQueue(maxsize=2)
queue_minute = queue.LifoQueue(maxsize=2)
queue_second = queue.LifoQueue(maxsize=2)
queue_satelitenumber = queue.LifoQueue(maxsize=2)
"""Save data from uart to queue"""


def getDataToQueue():
    print("run save data to queue")
    while True:

        stm32 = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)
        time.sleep(0.1)
        try:
            stm32.inWaiting() == 0
        except:
            print("No data")
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
        queue_temp.put(temp)
        queue_humid.put(humid)
        queue_hour.put(hour)
        queue_minute.put(minute)
        queue_second.put(second)
        queue_satelitenumber.put(satelitenumber)
        print(splitdata)
    # self.queue.put(None)


def sendtempandhumidto_apllication():
    # dopisać kolejki do kolejnych danych i funkcje je odbierające

    while True:
        temp = queue_temp.get()
        '''
        if temp is None:
        break
        '''
        print('consumer', temp)
        return temp
    '''
          stm32 = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)
          time.sleep(0.1)
          while(stm32.inWaiting()==0):
                
                
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
