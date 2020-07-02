#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    

    MOVIE:
    mid
    movie_name
    release_date

'''
import sqlite3
import random
from sqlite3 import Error

database = "movie.db"

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
    
    sql = ''' INSERT INTO MOVIE (MOVIE_NAME, RELEASE_DATE) 
            VALUES (:name, :release_date) '''
    cur = conn.cursor()
    
    movie_obj = {
        'name' : 'Thani Oruvan',
        'release_date' : '28 Aug 2015'
    }
    
    created_id = -1
    try:
        cur.execute(sql, movie_obj)
        
        created_id = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        #print('clean up')
        conn.commit()
    
    print('created id : '+str(created_id))

if __name__ == '__main__':
    start()        