#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:00:51 2021
Main Window aplication
@author: rafal
"""
import concurrent.futures
import sys
from threading import Thread
import time
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow, QApplication
import random
import wypis
from login1 import Ui_Login
from mainapi import Ui_MainWindow
from savedatathread import Savedatathread
from uart import  DataSaveToQueue
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Application(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.su = Savedatathread()

        self.DataSaveToQueue = DataSaveToQueue()
        self.ui.log_inButton.clicked.connect(self.getLoginPassword)  # self.getLoginPassword
        self.ui.make_mesurment.clicked.connect(self.lcdtempandhumid)  # self.getTemperature
        self.ui.koniecButton.clicked.connect(self.off_saveDataToDatabese)
        self.ui.checkBox.stateChanged.connect(self.state_checkedBox)
        self.ui.checkBox_2.stateChanged.connect(self.state_checkedBox)
        self.ui.checkBox_3.stateChanged.connect(self.state_checkedBox)
        self.ui.tabMap.currentChanged.connect(self.startFunctiononClick_tabMap)


        self.stateThread = 0
        self.openthreadofdatatoqueue()
        #self.startFunctiononClick_tabMap()
    """Start process for the tabMap index on the top"""

    def startFunctiononClick_tabMap(self):
        index = self.ui.tabMap.currentIndex()
        self.onTheTopIndex = 0
        # print(self.index)
        if index == 0:

            self.onTheTopIndex = 0
            print("Currently selected index -", self.onTheTopIndex)

                #Utworzyć wątek w któreym bedzie zwracana wartośc przez ThreadPoolExecutor wartość z innego wątku
            self.threadviewtempandhumid = Thread(target=self.dataviewtempandhumid, daemon=True).start()

            '''
            self.onTheTopIndex = 0
            self.t33 = Thread(target=self.lcdtempandhumid)
            self.t33.setDaemon(True)
            self.t33.start()
            '''
        if index == 1:
            self.onTheTopIndex = 1
            print("Currently selected index -", self.onTheTopIndex)
            # add functionality
            pass
        if index == 2:
            self.onTheTopIndex = 2
            print("Currently selected index -", self.onTheTopIndex)
            # add functionality
            pass

        if index == 3:
            self.onTheTopIndex = 3
            print("Currently selected index -", self.onTheTopIndex)
            # add functionality
            pass
        if index == 4:
            self.onTheTopIndex = 4
            print("Currently selected index -", self.onTheTopIndex)
            # add functionality




    """Function for koniecButton to off save Data to Database from tabMap"""

    def off_saveDataToDatabese(self):
        self.su.terminate()

    """Open login window and check the password and login user"""

    def getLoginPassword(self):
        d = Login()
        d.exec()

        print("Exit")

    """Get data from Queue from DataToQueue and show them in QLCDNumber"""
    def openthreadofdatatoqueue(self):
        self.threadsavetoqueue = Thread(target=self.DataSaveToQueue.savedata, daemon=True).start()



    def dataviewtempandhumid(self):
        """add functionality or remove function"""
        print('run thread')

        while self.onTheTopIndex == 0:

            t = self.DataSaveToQueue.queue_temp.get()
            h = self.DataSaveToQueue.queue_humid.get()
            self.ui.temp.display('{0:1d}'.format(int(t)))
            self.ui.humid.display('{0:1d}'.format(int(h)))
            time.sleep(2)
        print('end thread')


    """Show temperature and himidity in QLCDNumber temp and humid"""

    def lcdtempandhumid(self):
        self.ix = self.DataSaveToQueue.senddatatosisplay()

        self.ui.temp.display('{0:1d}'.format(int(self.ix)))





            #self.ui.temp.display('{0:1d}'.format(int(self.r)))

            #self.ui.temp.display('{0:1d}'.format(int(self.humidity)))

    """Check the marked boxes and run new Thread to save data"""

    def state_checkedBox(self, state):

        if state == 2:

            if self.sender() == self.ui.checkBox:

                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                logging.info("Run")
                self.t1 = Thread(target=self.su.run, args=(5,))
                # setDaemon(True) the thread exits with the main thread
                self.t1.setDaemon(True)
                self.t1.start()

            elif self.sender() == self.ui.checkBox_2:
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                pass


            elif self.sender() == self.ui.checkBox_3:

                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)



class Login(QDialog, Ui_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.log = Ui_Login()
        self.log.setupUi(self)
        self.log.login_Button.clicked.connect(self.loginfunction)

    def loginfunction(self):
        wypis.connectData(self)
        user = self.log.LineEdit_email.text()
        password1 = self.log.LineEdit_password.text()
        self.li = wypis.takeDataFromDatabase_password(self, user, password1)
        if self.li != 0:
            self.close()
        else:
            self.log.errorpassword.setText("Please input all fields.")


if __name__ == "__main__":
    logging.info("Apllication Run")
    app = QApplication(sys.argv)
    win = Application()
    win.show()
    sys.exit(app.exec_())

'''
self.t3 = Thread(target=self.su.run, args=(20,))
self.t3.setDaemon(True)
self.t3.start()

self.t1 = concurrent.futures.ThreadPoolExecutor()
self.tt1 = self.t1.submit(sendtempandhumidto_apllication)
self.r = self.tt1.result()
print(self.r)

self.t0 = concurrent.futures.ThreadPoolExecutor()
                self.t00 = self.t0.submit(self.DataSaveToQueue.senddatatosisplay)
                self.r = self.t00.result()
                time.sleep(1)
                self.ui.temp.display('{0:1d}'.format(int(self.r)))

'''