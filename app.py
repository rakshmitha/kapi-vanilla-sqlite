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
