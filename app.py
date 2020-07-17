from flask import Flask, jsonify, request, make_response
import sqlite3
import zenv
from sqlite3 import Error
from bubble_crud import *
database = zenv.DB_LOCATION
import delete as d
import delete_all as delete
import select_1 as sel
import update as up
import movie_collector_wiki as movie
import xlsx_reader as read

def get_db():

    conn = sqlite3.connect(database)
    return conn


app = Flask(__name__)

'''
http://0.0.0.0:5001/start

'''

@app.route("/", methods=['GET'])
def index():
    result = select_all(get_db())
    return make_response(jsonify(result=result), 200)

'''
http://0.0.0.0:5001/start

'''

@app.route("/start", methods=['GET'])
def start():
    result = d.start()
    return make_response(jsonify(result=result), 200)

'''
http://0.0.0.0:5001/delete_all

'''
    
@app.route("/delete_all", methods=['GET'])
def delete_all():
    result = delete.delete_all()
    return make_response(jsonify(result=result), 200)

'''
http://0.0.0.0:5001/select_1

'''

@app.route("/select_1", methods=['GET'])
def select_1():
    result = sel.select_1()
    return make_response(jsonify(result=result), 200)

'''
http://0.0.0.0:5001/update

'''
@app.route("/update", methods=['GET'])
def update():
    result = up.update()
    return make_response(jsonify(result=result), 200)


'''
http://0.0.0.0:5001/movie_collector_wiki

'''
@app.route("/movie_collector_wiki", methods=['GET'])
def movie_collector_wiki():
    result = movie.movie_collector_wiki()
    return make_response(jsonify(result=result), 200)





# def select_all():
#     """
#     Query all rows in the MOVIE table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = get_db().cursor()
#     cur.execute("SELECT * FROM MOVIE")

#     rows = cur.fetchall()

#     print('rows count : '+str(len(rows)))

#     if(len(rows) <= 0):
#         print('No Data available')
#         return ('No Data available')
#     return jsonify(rows)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
