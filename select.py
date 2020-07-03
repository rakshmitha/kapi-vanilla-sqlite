#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    
'''
import sqlite3
import random
from sqlite3 import Error

database = "kapi.db"

def start():
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        print(e) 
        return
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM MOVIE")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
 
    for row in rows:
        print(row)

if __name__ == '__main__':
    start()        