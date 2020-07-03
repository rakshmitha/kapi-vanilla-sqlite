#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    https://stackoverflow.com/questions/2942889/reading-parsing-excel-xls-files-with-python
'''
# import pandas as pd
import xlrd

BASE_FOLDER = "/Users/rajacsp/d/artisttics/artists/"
FILENAME = BASE_FOLDER + "kapi.xlsx"

def read_movies(sheet):

    for rowx in range(sheet.nrows):
        values = sheet.row_values(rowx)
        # print((values))

        movie_name, starring, direction, release_month, release_date = None, None, None, None, None
        actor, actress, comedian, production_house, critic_rating = None, None, None, None, None
        viewer_rating = None

        movie_name = values[0]
        starring = values[1]
        direction = values[2]
        release_month = values[3]
        release_date  = values[4] 

        actor = values[5]
        actress = values[6]
        comedian = values[7]
        production_house = values[8]
        critic_rating = values[9]

        # print(comedian)

def read_artists(sheet):

    for rowx in range(sheet.nrows):
        values = sheet.row_values(rowx)
        # print((values))    

        name, original_name, dob, location, country, income, description = None, None, None, None, None, None, None

        name = values[0]
        original_name = values[1]
        dob = values[2]
        location = values[3]
        country = values[4]
        income = values[5]
        description = values[6]

        if(len(name) <= 1):
            continue

        if(name == 'NA'):
            continue
        
        if(name == 'Name'):
            continue
        # print(country)

        # Insert base sql
        # insert_sql = "INSERT INTO PUBLIC_ARTIST (ARTIST_NAME, DOB, LOCATION, COUNTRY) VALUES ('"+str(name)+"', '01 01 1993', '"+str(location)+"', '"+str(country)+"');"
        # print(insert_sql)

        if(len(description) < 2):
            continue

        description = description.replace("\"", "'")

        # Update description
        update_sql = "UPDATE PUBLIC_ARTIST SET DESCRIPTION = \""+str(description)+"\" WHERE ARTIST_NAME = '"+str(name)+"';"
        print(update_sql)



def read_xlsx():

    workbook = xlrd.open_workbook(FILENAME)

    # read_movies(workbook.sheet_by_index(0))

    read_artists(workbook.sheet_by_index(1))

def start():
    read_xlsx()

if __name__ == '__main__':
    start()        