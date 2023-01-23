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

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow, QApplication

import wypis
from login1 import Ui_Login
from mainapi import Ui_MainWindow
from savedatathread import Savedatathread
from uart import sendtempandhumidto_apllication, getDataToQueue


class Application(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.su = Savedatathread()
        #self.saveDataToQueue = DataToQueue()
        self.ui.log_inButton.clicked.connect(self.getLoginPassword)  # self.getLoginPassword
        self.ui.make_mesurment.clicked.connect(self.lcdtempandhumid)  # self.getTemperature
        self.ui.koniecButton.clicked.connect(self.off_saveDataToDatabese)
        self.ui.checkBox.stateChanged.connect(self.state_checkedBox)
        self.ui.checkBox_2.stateChanged.connect(self.state_checkedBox)
        self.ui.checkBox_3.stateChanged.connect(self.state_checkedBox)
        self.ui.tabMap.currentChanged.connect(self.startFunctiononClick_tabMap)
        # self.startFunctiononClick_tabMap()

        self.stateThread = 0
        self.openthreadofdatatoqueue()
    """Start process for the tabMap index on the top"""

    def startFunctiononClick_tabMap(self):
        index = self.ui.tabMap.currentIndex()
        self.onTheTopIndex = 0
        # print(self.index)
        if index == 0:
            self.onTheTopIndex = 0
            '''
            self.t1 = concurrent.futures.ThreadPoolExecutor()
            self.tt1 = self.t1.submit(self.lll.getDataBuffer)  # print(self.tt1)
            '''
        if index == 1:
            self.onTheTopIndex = 1
            # add functionality
            pass
        if index == 2:
            self.onTheTopIndex = 2
            # add functionality
            pass

        if index == 3:
            self.onTheTopIndex = 3

        if index == 4:
            self.onTheTopIndex = 4

            self.lcdtempandhumid()

            '''
            self.t3 = Thread(target=self.consumer.producer)
            self.t3.setDaemon(True)
            self.t3.start()
            '''

        else:

            print("Currently selected index - {0:1d}".format(self.onTheTopIndex))

    """Function for koniecButton to off save Data to Database from tabMap"""

    def off_saveDataToDatabese(self):
        self.su.terminate()

    """Open login window and check the password and login user"""

    def getLoginPassword(self):
        d = Login()
        d.exec()

        print("Exiting")

    """Get data from Queue from DataToQueue and show them in QLCDNumber"""
    def openthreadofdatatoqueue(self):
        self.threadsavetoqueue = Thread(target=getDataToQueue)
        self.threadsavetoqueue.setDaemon(True)
        self.threadsavetoqueue.start()

    def get_tempandhumid(self):
        """add functionality or remove function"""
        pass

    """Show temperature and himidity in QLCDNumber temp and humid"""

    def lcdtempandhumid(self):
        self.t1 = concurrent.futures.ThreadPoolExecutor()
        self.tt1 = self.t1.submit(sendtempandhumidto_apllication)
        self.r = self.tt1.result()
        print(self.r)


        """add functionality or remove function"""

        self.ui.temp.display('{0:1d}'.format(int(self.r)))
        #self.ui.temp.display('{0:1d}'.format(int(self.humidity)))

    """Check the marked boxes and run new Thread to save data"""

    def state_checkedBox(self, state):

        if state == 2:

            if self.sender() == self.ui.checkBox:

                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                print("run")

                # self.t1 = self.ThreadPoolExecutor(max_workers=1)
                # self.tt1 = self.t1.submit(self.su.run)

                self.t1 = Thread(target=self.su.run, args=(5,))
                # setDaemon(True) the thread exits with the main thread
                self.t1.setDaemon(True)
                self.t1.start()

            elif self.sender() == self.ui.checkBox_2:
                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_3.setChecked(False)
                pass

                self.t2 = Thread(target=self.su.run, args=(15,))

                self.t2.setDaemon(True)
                self.t2.start()

            elif self.sender() == self.ui.checkBox_3:

                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                pass

                self.t3 = Thread(target=self.su.run, args=(20,))
                self.t3.setDaemon(True)
                self.t3.start()


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
    app = QApplication(sys.argv)
    win = Application()
    win.show()
    sys.exit(app.exec_())
