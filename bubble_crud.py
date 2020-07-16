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

    # return('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        return('No Data available')
    return rows
    # for row in rows:
    #     print(row)


def select_all_by_actor(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM COARTIST_BUBBLE WHERE ARTIST_NAME LIKE '%"+actor_name+"%'")

    rows = cur.fetchall()

    #print('rows count : '+str(len(rows)))

    if(len(rows) <= 0):
        return('No Data available')

    for row in rows:
        return(row)


def add_coartist_bubble(conn, bubble_obj):
    """
    Create a movie
    :param task:
    :return: task id
    """

    sql = ''' INSERT INTO COARTIST_BUBBLE (ARTIST_NAME, COARTIST_CATEGORY, COARTIST_NAME, BUBBLE_SCORE) 
            VALUES (:artist_name, :coartist_category, :coartist_name, :bubble_score) '''
    cur = conn.cursor()

    lastrowid = -1
    try:
        cur.execute(sql, bubble_obj)

        lastrowid = cur.lastrowid
    except sqlite3.IntegrityError as sqle:
        return("SQLite error : {0}".format(sqle))
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

    sql = ''' DELETE FROM MOVIE '''
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

        # CREATE
        # :artist_name, :coartist_category, :coartist_name, :bubble_score
        print('Create Coartist Bubble')
        bubble_obj = {
            'artist_name': 'Dhanush',
            'coartist_category': 'actress',
            'coartist_name': 'Kajal Agarwal',
            'bubble_score': 70
        }
        result = add_coartist_bubble(conn, bubble_obj)
        print(result)
        print('---------------\n')

        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        print('Read Coartist Bubble by Name')
        select_all_by_actor(conn, 'Dhanush')
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
