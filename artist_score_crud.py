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

import zenv

database = zenv.DB_LOCATION

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

    sql = """
    SELECT
        PA.AID AS 'ARTIST_ID',
        PA.ARTIST_NAME AS 'ARTIST_NAME',
        ASCORE.YEAR  AS 'ARTIST_YEAR',
        ASCORE.CRITIC_SCORE AS 'CRITIC_SCORE',
        ASCORE.AUDIENCE_SCORE AS 'AUDIENCE_SCORE',
        ASCORE.BOX_OFFICE_SCORE AS 'BOX_OFFICE_SCORE'
    FROM ARTIST_SCORE ASCORE
    INNER JOIN PUBLIC_ARTIST PA ON PA.AID = ASCORE.ARTIST_ID
    WHERE PA.ARTIST_NAME = :actor_name
    """

    actor_obj = {
        'actor_name' : actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, actor_obj)
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
 
    for row in rows:
        print(row) 


def add_artist_score_crud(conn, bubble_obj):
    """
    Create an Artist Score
    :param task:
    :return: task id
    """

#     CREATE TABLE "ARTIST_SCORE" (
# 	"ASID"	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	"ARTIST_NAME"	TEXT NOT NULL,
# 	"YEAR"	INTEGER NOT NULL,
# 	"CRITIC_SCORE"	INTEGER NOT NULL,
# 	"AUDIENCE_SCORE"	INTEGER NOT NULL,
# 	"BOX_OFFICE_SCORE"	INTEGER NOT NULL
# );

    sql = ''' INSERT INTO ARTIST_SCORE (ARTIST_NAME, YEAR, CRITIC_SCORE, AUDIENCE_SCORE, BOX_OFFICE_SCORE) 
            VALUES (:artist_name, :year, :critic_score, :audience_score, :box_office_score) '''
    cur = conn.cursor()
    
    lastrowid = -1
    try:
        cur.execute(sql, bubble_obj)
        
        lastrowid = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        print("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return lastrowid

def update_movie(conn, bubble_obj):
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
        cur.execute(sql, bubble_obj)
        
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
        # :artist_name, :year, :critic_score, :audience_score, :box_office_score
        # print('Create Aritst Score')
        # bubble_obj = {
        #     'artist_name' : 'Dhanush',
        #     'year' : 2018,
        #     'critic_score' : 82,
        #     'audience_score' : 77,
        #     'box_office_score' : 90
        # } 
        # result = add_artist_score_crud(conn, bubble_obj)
        # print(result)
        # print('---------------\n')
    
        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        print('Read Coartist Bubble by Name')
        select_all_by_actor(conn, 'Vijay')
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