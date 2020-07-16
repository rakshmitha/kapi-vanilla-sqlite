import artist_score_crud as ASCO
from flask import Flask, jsonify, request, make_response
import sqlite3
import zenv
from sqlite3 import Error
from bubble_crud import *
database = zenv.DB_LOCATION


def get_db():

    conn = sqlite3.connect(database)
    return conn


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    result = select_all(get_db())
    return make_response(jsonify(result), 200)


''' START OF MY WORK - KARTHIK '''

''' artist_score_crud'''

''' Routes '''

''' select all by actor name : route - /select-all-by-actor-name/Dhanush'''


@app.route("/select-all-by-actor-name/<actor_name>")
def select_all_by_actor_name(actor_name):
    result = ASCO.select_all_by_actor(get_db(), actor_name)
    return make_response(jsonify(result), 200)


''' select coartist bubble by artist : route - /select-coartist-bubble-by-artist '''


@app.route("/select-coartist-bubble-by-artist/<actor_name>")
def select_coartist_bubble_by_artist(actor_name):
    result = ASCO.select_coartist_bubble_by_artist(get_db(), actor_name)
    return make_response(jsonify(result), 200)


''' /add-artist-score-crud '''


@app.route("/add-artist-score-crud")
def add_artist_score_crud():
    obj = request.get_json(force=True)
    result = ASCO.add_artist_score_crud(get_db(), obj)
    return make_response(jsonify(result), 200)


''' /update-movie-asco '''


@app.route("/update-movie-asco")
def update_movie():
    obj = request.get_json(force=True)
    result = ASCO.update_movie(get_db(), obj)
    return make_response(jsonify(result), 200)


'''  /delete-movie-asco/Asuran  '''


@app.route("/delete-movie-asco/<movie_name>")
def delete_movie(movie_name):
    result = ASCO.delete_movie(get_db(), movie_name)
    return make_response(jsonify(result), 200)


'''  /delete-all-movies-asco '''


@app.route("/delete-all-movies-asco")
def delete_all_movies():
    result = ASCO.delete_all_movies(get_db())
    return make_response(jsonify(result), 200)


''' END OF MY WORK - KARTHIK '''

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
    app.run(debug=True)
