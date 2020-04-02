import pymysql
from flask import Flask, request
from flask import Response
from service import user_service
import json

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    payload = request.get_json()
    user_service.create_user(payload)
    return Response(json.dumps(payload), status=201, mimetype='application/json')


@app.route('/users', methods=['GET'])
def get_user():
    id_user = request.args.get("id_user")
    user = user_service.select_user(id_user)
    return Response(user, status=200, mimetype='application/json')


'''
@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.select_all_users()
    print(users)
    return Response(users, status=200, mimetype='application/json')
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
