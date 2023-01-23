#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:11:08 2021

@author: rafal
"""

import mysql.connector
from mysql.connector import errorcode
#from login1 import Ui_Login
#from apiUI import Login
'''
class connectDataMysql():
    def __init__(self, parent=None):
        self.logg = Ui_Login()
        self.logg.setupUi(self)
        self.connectData()
        #self.writeDataOn_Console()
        self.takeDataFromDatabase_password()
        '''
def connectData(self):
        self.config = {
                'user': "phpmyadmin",
                'password': "97354929_M" ,
                'host': "localhost",
                'database': "apiUI",
                'raise_on_warnings': True
                }
        '''
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="phpmyadmin",
        password="97354929_M",
        database="Users"
        )
        '''
        try:
            self.mydb = mysql.connector.connect(**self.config)
            print("connected")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doe not exist")
            else:
                print(err)

def writeDataOn_Console(self):
        
        sql_select_Query = "select login from USERS"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql_select_Query)
        result = mycursor.fetchall()
        print ("Total number of rows in table ", mycursor)
        print("\nPronting each row")

        for x in result:
            print(x)

def takeDataFromLineEdit_password(self):
        
        user =  1
        password = 2
        if (user == ('123')) or (password ==('1234')):
            print ('Login_successful')
            self.close()
        elif len(user)==0 or len(password)==0:
            self.log.errorpassword.setText("Please input all fields.")
           
        else:
            print(password)
            
def takeDataFromDatabase_password(self, user , password1):
        username = user
        password = password1
        sql_question =  """SELECT login , password , login_id, id_login 
                         FROM LOGIN_apiUI, PASSWORD_apiUI 
                         WHERE login ='%s' 
                         AND password ='%s' 
                         AND login_id = id_login """ % (username, password)
        coursor = self.mydb.cursor()
        coursor.execute(sql_question)
        self.answer = coursor.fetchone()
        #print(len(answer))
        print(self.answer)
        if( self.answer != None):
            dataFromDatabases = []
            for row in self.answer:
                print(row)
                dataFromDatabases.append(row)
            log = dataFromDatabases[0]
            pa  = dataFromDatabases[1]
            if (log == username or pa == password):
            
                print('log is ok')
                return 1
            else:
                print ('sorry some one is wrong')
                return 0 
        else:
            return 0



'''
"""

        

                          SELECT PASSWORD_apiUI.password, LOGIN_apiUI.login 
                          FROM LOGIN_apiUI 
                          JOIN PASSWORD_apiUI 
                          ON id_login = login_id;
                          """

for x in result:
    print("Id = " , x[0],)
    print("login = ",x[1])
    print("password = ",x[2])
print ("Operation was successful")


'''
