from flask import Flask, jsonify, request, make_response
import sqlite3
import zenv
from sqlite3 import Error
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
def update_movie():
        obj=request.get_json(force=True)
        print("JSON INPUT ::::  \n",obj)
        result = bc.update_movie(get_db(),obj)
        return make_response(jsonify(result), 200)




'''
http://127.0.0.1:5001/delete-movie/<name>
'''
@app.route("/delete-movie/<name>")
def delete_movie(name):
    result = bc.delete_movie(get_db(),name)
    return make_response(jsonify(result), 200)


'''
http://127.0.0.1:5001/delete-all-cities
'''
@app.route("/delete-all-cities")
def delete_all_cities():
    result = bc.delete_all_cities(get_db())
    return make_response(jsonify(result), 200)
       
'''
http://127.0.0.1:5001/add-movie/<name>/<releasedate>/<starring>
'''
@app.route("/add-movie/<name>/<releasedate>/<starring>")
def add_movie(name,releasedate,starring):
    result = ins.add_movie(name,releasedate,starring)
    return make_response(jsonify(result), 200)



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
