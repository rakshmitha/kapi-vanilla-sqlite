from flask import Flask, jsonify, request, make_response
import sqlite3
import zenv
from sqlite3 import Error
import artist_score_crud as ASCO
import movie_basic_crud as MBC
import bubble_crud as bc
import insert as ins
database = zenv.DB_LOCATION


def get_db():

    conn = sqlite3.connect(database)
    return conn


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    result = bc.select_all(get_db())
    return make_response(jsonify(result), 200)

'''Started - Gokul'''
'''artist_score_crud - Gokul'''

'''
select_all
http://0.0.0.0:5001/select_all
'''
@app.route("/select_all", methods=['GET'])
def select_all():
    result = ASCO.select_all(get_db())
    return make_response(jsonify(result), 200)

'''
get_actor_id
http://0.0.0.0:5001/get_actor_id/Dhanush
'''
@app.route("/get_actor_id/<actor_name>", methods=['GET'])
def get_actor_id(actor_name):
    result = ASCO.get_actor_id(get_db(),actor_name)
    return make_response(jsonify(result), 200)

'''
get_actor_details_by_name
http://0.0.0.0:5001/get_actor_details_by_name/Dhanush
'''
@app.route("/get_actor_details_by_name/<actor_name>", methods=['GET'])
def get_actor_details_by_name(actor_name):
    result = ASCO.get_actor_details_by_name(get_db(),actor_name)
    return make_response(jsonify(result), 200)

'''
select_all_artits
http://0.0.0.0:5001/select_all_artits/10/5
NameError: name 'actor_name' is not defined
'''
@app.route("/select_all_artits/<limit>/<offset>", methods=['GET'])
def select_all_artits(limit,offset):
    result = ASCO.select_all_artits(get_db(),limit,offset)
    return make_response(jsonify(result), 200)

'''movie_basic_crud - Gokul'''

'''
select_all_movies_with_artists_by_movie_name
http://0.0.0.0:5001/select_all_movies_with_artists_by_movie_name/Asuran
'''
@app.route("/select_all_movies_with_artists_by_movie_name/<movie_name>", methods=['GET'])
def select_all_movies_with_artists_by_movie_name(movie_name):
    result = MBC.select_all_movies_with_artists_by_movie_name(get_db(),movie_name)
    return make_response(jsonify(result), 200)

'''
select_all_movies_by_actor_name
http://0.0.0.0:5001/select_all_movies_by_actor_name/Dhanush
'''
@app.route("/select_all_movies_by_actor_name/<actor_name>", methods=['GET'])
def select_all_movies_by_actor_name(actor_name):
    result = MBC.select_all_movies_by_actor_name(get_db(),actor_name)
    return make_response(jsonify(result), 200)

'''
add_movie
http://0.0.0.0:5001/add_movie
'''
@app.route("/add_movie", methods=['GET'])
def add_movie():
    obj=request.get_json(force=True)
    result = MBC.add_movie(get_db(),obj)
    return make_response(jsonify(result), 200)

'''
update_movie
http://0.0.0.0:5001/update_movie
'''
@app.route("/update_movie", methods=['GET'])
def update_movie():
    obj=request.get_json(force=True)
    result = MBC.update_movie(get_db(),obj)
    return make_response(jsonify(result), 200)

'''
delete_movie
http://0.0.0.0:5001/delete_movie/Asuran
'''
@app.route("/delete_movie/<name>", methods=['GET'])
def delete_movie(name):
    result = MBC.delete_movie(get_db(),name)
    return make_response(jsonify(result), 200)

'''
delete_all_cities
http://0.0.0.0:5001/delete_all_cities
'''
@app.route("/delete_all_cities", methods=['GET'])
def delete_all_cities():
    result = MBC.delete_all_cities(get_db())
    return make_response(jsonify(result), 200)
    
'''Ended - Gokul'''

'''Started - Vaishnavi V'''

'''
    http://127.0.0.1:5001/select-all-by-actor/<actor_name>
'''

@app.route("/select-all-by-actor/<actor_name>")
def select_all_by_actor(actor_name):
        result = bc.select_all_by_actor(get_db(),actor_name)
        return make_response(jsonify(result), 200)

'''
    http://127.0.0.1:5001/add-coartist-bubble
'''
@app.route("/add-coartist-bubble")
def add_coartist_bubble():
        obj=request.get_json(force=True)
        print("JSON INPUT ::::  \n",obj)
        result = bc.add_coartist_bubble(get_db(),obj)
        return make_response(jsonify(result), 200)

'''
    http://127.0.0.1:5001/update-movie
'''
@app.route("/update-movie")
def update_movie_bc():
        obj=request.get_json(force=True)
        print("JSON INPUT ::::  \n",obj)
        result = bc.update_movie(get_db(),obj)
        return make_response(jsonify(result), 200)




'''
http://127.0.0.1:5001/delete-movie/<name>
'''
@app.route("/delete-movie/<name>")
def delete_movie_bc(name):
    result = bc.delete_movie(get_db(),name)
    return make_response(jsonify(result), 200)


'''
http://127.0.0.1:5001/delete-all-cities
'''
@app.route("/delete-all-cities")
def delete_all_cities_bc():
    result = bc.delete_all_cities(get_db())
    return make_response(jsonify(result), 200)
       
'''
http://127.0.0.1:5001/add-movie/<name>/<releasedate>/<starring>
'''
@app.route("/add-movie/<name>/<releasedate>/<starring>")
def add_movie_bc(name,releasedate,starring):
    result = ins.add_movie(name,releasedate,starring)
    return make_response(jsonify(result), 200)

'''Ended - Vaishnavi V'''


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
