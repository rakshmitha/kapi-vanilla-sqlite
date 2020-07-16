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

import zenv

database = zenv.DB_LOCATION

def add_movie(name, release_date, starring):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        return(e) 
        
    
    sql = ''' INSERT INTO MOVIE (MOVIE_NAME, RELEASE_DATE, STARRING) 
            VALUES (:name, :release_date, :starring) '''
    cur = conn.cursor()
    
    movie_obj = {
        'name' : name,
        'release_date' : release_date,
        'starring' : starring
    }
    
    created_id = -1
    try:
        cur.execute(sql, movie_obj)
        
        created_id = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
    finally:
        #print('clean up')
        conn.commit()
    
    return('created id : '+str(created_id))

def start():
    
    add_movie('Thanga Magan', '18 Dec 2015', 'Dhanush, Amy Jackson, Samantha Ruth Prabhu')

if __name__ == '__main__':
    start()        