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

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def select_all(conn):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM MOVIE")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
 
    for row in rows:
        print(row)         

def select_all_by_actor(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM MOVIE WHERE STARRING LIKE '%"+actor_name+"%'")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
 
    for row in rows:
        print(row) 


def add_movie(conn, movie_obj):
    """
    Create a movie
    :param task:
    :return: task id
    """
   
    sql = ''' INSERT INTO MOVIE (MOVIE_NAME, RELEASE_DATE, STARRING) 
            VALUES (:name, :release_date, :starring) '''
    cur = conn.cursor()
    
    lastrowid = -1
    try:
        cur.execute(sql, movie_obj)
        
        lastrowid = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return lastrowid

def update_movie(conn, movie_obj):
    """
    Create a movie
    :param movie object:
    :return: None
    """
   
    sql = ''' UPDATE MOVIE
    SET MOVIE_NAME = :new_name, 
    STARRING = :starring,
    RELEASE_DATE = :release_date 
    WHERE MOVIE_NAME = :name '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql, movie_obj)
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Updated')
    
def delete_movie(conn, name):
    """
    Delete a movie
    :param movie object:
    :return: None
    """
   
    sql = ''' DELETE FROM MOVIE    
    WHERE MOVIE_NAME = ?'''
    cur = conn.cursor()
    
    try:
        cur.execute(sql, (name,))
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Deleted')
    
def delete_all_cities(conn):
    """
    Delete a movie
    :param movie object:
    :return: None
    """
   
    sql = ''' DELETE MOVIE '''
    cur = conn.cursor()
    
    try:
        cur.execute(sql)
        
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    print('Delete')        

def main():    
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:        
        
        # CREATE
        # print('Create Movie')
        # movie_obj = {
        #     'name' : 'Dharbar',
        #     'release_date' : '9 Jan 2020',
        #     'starring' : 'Rajini, Nayanthara'
        # } 
        # result = add_movie(conn, movie_obj)
        # print(result)
        # print('---------------\n')
    
        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        print('Read Movie by Name')
        select_all_by_actor(conn, 'Rajini')
        print('---------------\n')
        
        # UPDATE
        # print('Update Movie')
        # city_new_obj = {
        #     'name' : 'Asuran',
        #     'new_name' : 'Asuran',
        #     'starring' : 'Dhanush, TeeJay, Ken Karunas',
        #     'release_date' : '4 Oct 2019'
        # }
        # update_movie(conn, city_new_obj)
        # print('---------------\n')
        
        # DELETE    
        # print('Delete Movie')  
        # delete_movie(conn, 'Kadal')
        # print('---------------\n')
        
if __name__ == '__main__':
    main()        