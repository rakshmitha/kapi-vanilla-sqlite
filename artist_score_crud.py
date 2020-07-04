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
import sys

import zenv
import random_world as ranwo
import movie_basic_crud as mcrud

database = zenv.DB_LOCATION

active_years = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020
]

def make_artist_score_insert_sql(conn, actor_name):

    artist_id = get_actor_id(conn, actor_name)

    # print('artist_id : ', artist_id)

    for c_year in active_years:
        # print(c_year)

        r_critic_score = ranwo.get_random_score(60, 100)
        r_audience_score = ranwo.get_random_score(60, 100)
        r_box_office_score = ranwo.get_random_score(60, 100)

        r_ip = ranwo.get_random_ip()

        sql = "INSERT INTO ARTIST_SCORE (ARTIST_ID, YEAR, CRITIC_SCORE, AUDIENCE_SCORE, BOX_OFFICE_SCORE, USER_IP, USERID, UPDATED_AT) VALUES ("+str(artist_id)+", "+str(c_year)+", "+str(r_critic_score)+", "+str(r_audience_score)+", "+str(r_box_office_score)+", '"+str(r_ip)+"', NULL, DATE());"

        print(sql)

def make_coartist_bubble_score_insert_sql(conn, actor_name):

    artist_id = get_actor_id(conn, actor_name)

    # print('artist_id : ', artist_id)

    movie_list = mcrud.select_all_movies_by_actor_name(conn, actor_name)

    for movie in movie_list:
        # print(movie)

        movie_artist_list = mcrud.select_all_movies_with_artists_by_movie_name(conn, movie['movie_name'])

        for movie_artist in movie_artist_list:

            # print('movie_name : ', movie_artist['movie_name'])

            if(movie_artist['artist_id'] == artist_id):
                # print('Same Actor, so skipping')
                continue

            c_artist_id = artist_id
            c_artist_category = 'starring' # hardcoded as we use only actors now
            c_coartist_id = movie_artist['artist_id']
            c_coartist_category = movie_artist['artist_role']
            c_bubble_score = ranwo.get_random_score(60, 100)

            c_user_ip = ranwo.get_random_ip()

            sql = "INSERT INTO COARTIST_BUBBLE (ARTIST_ID, ARTIST_CATEGORY, COARTIST_ID, COARTIST_CATEGORY, BUBBLE_SCORE, USER_IP, USERID, UPDATED_AT) "
            sql += "VALUES ("+str(c_artist_id)+", '"+str(c_artist_category)+"', "+str(c_coartist_id)+", '"+str(c_coartist_category)+"', "+str(c_bubble_score)+", '"+str(c_user_ip)+"', 0, DATE());" 

            print(sql)    

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

def get_actor_id(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """

    sql = """
    SELECT
	    PA.AID AS 'ARTIST_ID'
    FROM PUBLIC_ARTIST PA
    WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE;
    """

    actor_obj = {
        'actor_name' : actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, actor_obj)
 
    rows = cur.fetchall()
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
        return -1

    for row in rows:
        # print(row) 

        return row[0]

    return -1

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
        ASCO.YEAR  AS 'ARTIST_YEAR',
        ROUND(AVG(ASCO.CRITIC_SCORE), 2) AS 'CRITIC_SCORE',
        ROUND(AVG(ASCO.AUDIENCE_SCORE), 2) AS 'AUDIENCE_SCORE',
        ROUND(AVG(ASCO.CRITIC_SCORE), 2) AS 'BOX_OFFICE_SCORE'
    FROM ARTIST_SCORE ASCO
    INNER JOIN PUBLIC_ARTIST PA ON PA.AID = ASCO.ARTIST_ID
    WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE
    GROUP BY ASCO.YEAR
    """

    actor_obj = {
        'actor_name' : actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, actor_obj)
 
    rows = cur.fetchall()
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
 
    score_list = []
    for row in rows:
        # print(row) 

        score_dict = {
            'artist_id' : row[0],
            'artist_name' : row[1],
            'artist_year' : row[2],
            'critic_score' : row[3],
            'audience_score' : row[4],
            'box_office_score' : row[5]
        }

        score_list.append(score_dict)

    return score_list


def select_coartist_bubble_by_artist(conn, actor_name):
    """
    Query all rows in the MOVIE table
    :param conn: the Connection object
    :return:
    """

    sql = """
    SELECT
        ARTIST_ID,
        ARTIST_CATEGORY,
        COARTIST_ID,
        COARTIST_CATEGORY,
        COUNT(BUBBLE_SCORE) AS 'VOTE_COUNT',
        ROUND(AVG(BUBBLE_SCORE), 2) AS 'BUBBLE_SCORE'
    FROM COARTIST_BUBBLE COB
    INNER JOIN PUBLIC_ARTIST PA ON PA.AID = COB.ARTIST_ID
    WHERE PA.ARTIST_NAME = :actor_name COLLATE NOCASE
    GROUP BY COARTIST_ID
    """

    actor_obj = {
        'actor_name' : actor_name
    }

    cur = conn.cursor()
    cur.execute(sql, actor_obj)
 
    rows = cur.fetchall()
    
    # print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available')
        return None
 
    coartist_bubble_list = []
    for row in rows:
        print(row) 

        c_bubble_dict = {
            'arist_id' : row[0],
            'artist_category' : row[1],
            'coartist_id' : row[2],
            'coartist_category' : row[3],
            'vote_count' : row[4],
            'bubble_score' : row[5]
        }

        coartist_bubble_list.append(c_bubble_dict)

    return coartist_bubble_list


def add_artist_score_crud(conn, bubble_obj):
    """
    Create an Artist Score
    :param task:
    :return: task id
    """

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

def generate_artist_score(conn):

    if(not sys.argv[0]):
        print('No arguments provided, so skip it')
        return

    actor_name = sys.argv[1]

    # print('actor_name : ', actor_name)

    make_artist_score_insert_sql(conn, actor_name)

def generate_coartist_bubble_score_insert_sql(conn):

    if(not sys.argv[0]):
        print('No arguments provided, so skip it')
        return

    actor_name = sys.argv[1]

    # print('actor_name : ', actor_name)

    make_coartist_bubble_score_insert_sql(conn, actor_name)

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

        # Make sql
        # generate_artist_score(conn)

        # Make Coartist bubble score
        generate_coartist_bubble_score_insert_sql(conn)
    
        # READ
        # print('Read Movie')
        # select_all(conn)
        # print('---------------\n')

        # READ by Name
        # print('Read Coartist Bubble by Name')
        # actor_name = sys.argv[1]
        # select_all_by_actor(conn, actor_name)
        # print('---------------\n')
        
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