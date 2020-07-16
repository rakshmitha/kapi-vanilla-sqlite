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
import random_world as ranwo


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
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        return('No Data available')
 
    for row in rows:
        print(row)
    return rows         

def select_all_movies_with_artists_by_movie_name(conn, movie_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """

    sql = """
    SELECT
        MA.MOVIE_ID AS 'MOVIE_ID',
        M.MOVIE_NAME AS  'MOVIE_NAME',
        MA.ARTIST_ID AS 'ARTIST_ID',
        PA.ARTIST_NAME AS 'ARTIST_NAME',
        MA.ARTIST_ROLE AS 'ARTIST_ROLE'
    FROM MOVIE_ARTIST MA
    INNER JOIN MOVIE M ON M.MID = MA.MOVIE_ID
    INNER JOIN PUBLIC_ARTIST PA ON PA.AID = MA.ARTIST_ID
    WHERE M.MOVIE_NAME = :movie_name COLLATE NOCASE;
    """

    movie_obj = {
        'movie_name' : movie_name
    }

    cur = conn.cursor()
    cur.execute(sql, movie_obj)
 
    rows = cur.fetchall()
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        return('No Data available')
 
    movie_list = []
    for row in rows:
        # print(row) 

        cur_movie = {
            'movie_id' : row[0],
            'movie_name' : row[1],
            'artist_id' : row[2],
            'artist_name' : row[3],
            'artist_role' : row[4]
        }

        movie_list.append(cur_movie)

    # print('movie_list : ', movie_list)

    return movie_list

def select_all_movies_by_actor_name(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """

    sql = """
    SELECT
        M.MID AS 'MOVIE_ID',
        M.MOVIE_NAME AS  'MOVIE_NAME',
        M.RELEASE_DATE AS 'RELEASE_DATE'
    FROM MOVIE M
    INNER JOIN MOVIE_ARTIST MA ON M.MID = MA.MOVIE_ID
    INNER JOIN PUBLIC_ARTIST PA ON PA.AID = MA.ARTIST_ID
    WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE
    """

    movie_obj = {
        'actor_name' : actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, movie_obj)
 
    rows = cur.fetchall()
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        return('No Data available')
 
    movie_list = []
    for row in rows:
        # print(row) 

        cur_movie = {
            'movie_id' : row[0],
            'movie_name' : row[1],
            'release_date' : row[2]
        }

        movie_list.append(cur_movie)

    # print('movie_list : ', movie_list)

    return movie_list

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
        return("SQLite error : {0}".format(sqle))
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
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return('Updated')
    
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
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return('Deleted')
    
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
        return("SQLite error : {0}".format(sqle))
    finally:
        conn.commit()
    
    return('Delete')        

def main():    
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:  

        pass      
        
        # CREATE
        # print('Create Movie')
        # movie_obj = {
        #     'name' : 'Dharbar',
        #     'release_date' : '9 Jan 2020'
        # } 
        # result = add_movie(conn, movie_obj)
        # print(result)
        # print('---------------\n')

        # Make 
    
        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # Get all movies with artist by movie name
        # print('Read Movie with artists by Name ')
        # select_all_movies_with_artists_by_movie_name(conn, 'maari 2')
        # print('---------------\n')

        # Get all movies by artist name
        # select_all_movies_by_actor_name(conn, 'dhanush')
        # print('---------------\n')

        # # READ by Name
        # print('Read Movie with artists by Name ')
        # select_all_movies_with_artists_by_movie_name(conn, 'maari 2')
        # print('---------------\n')
        
        # UPDATE
        # print('Update Movie')
        # city_new_obj = {
        #     'name' : 'Asuran',
        #     'new_name' : 'Asuran'
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