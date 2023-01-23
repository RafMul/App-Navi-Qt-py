#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 20:38:02 2021

@author: rafal
"""

import mysql.connector
from mysql.connector import errorcode


class Login_database():
    def __init__(self, login, password, config, cnx):
        self.login = login
        self.password = password
        self.config = config
        self.cnx = cnx
        login = 'root'
        password = ''
        config = {
                'user': login,
                'password': password ,
                'host': '127.0.0.1',
                'database': 'aplikacja',
                'raise_on_warnings': True
                }

        try:
            #cnx = mysql.connector.connect(user='scott',database='employ')
            cnx = mysql.connector.connect(**self.config)
            print("connected")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doe not exist")
            else:
                print(err)
        else:
            cnx.close()
            
            
class Add_user(Login_database):
    def __init__():
        
        print('czesc')

class Send_DatatoDatabase():
      pass
    
Login_database() 
