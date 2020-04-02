import pymysql
import json
import datetime


def insert_user(json):
    db = connect_to_mysql("localhost", "rafael", "123", "management")
    cursor = db.cursor()
    cursor.execute(format_query(json))
    db.commit()
    db.close()


def select_all_users():
    db = connect_to_mysql("localhost", "rafael", "123", "management")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")

    all_users = cursor.fetchall()
    return all_users


def select_user(id_user):
    db = connect_to_mysql("localhost", "rafael", "123", "management")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE id_user = {}".format(id_user))

    user = cursor.fetchone()
    user_str = format_json(user)
    # print(user)
    return user_str


def format_json(data):
    dt_dict = {
        "id_user": data[0],
        "name": data[1],
        "gender": data[2],
        "dt_birth": (data[3]).strftime("%x"),
        "cep": data[4],
        "street": data[5],
        "complement": data[6],
        "neighborhood": data[7],
        "city": data[8],
        "state": data[9]
    }

    dt_json = json.dumps(dt_dict)

    return dt_json


def format_query(json):
    return "INSERT INTO user (id_user, name, gender, dt_birth, cep, street, complement, neighborhood, city, " \
           "state) VALUES " \
           "({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
        json['id_user'], json['name'], json['gender'], json['dt_birth'], json['cep'], json['street'],
        json['complement'], json['neighborhood'], json['city'], json['state'])


def connect_to_mysql(host, username, password, database):
    return pymysql.connect(host, username, password, database)


if __name__ == "__main__":

    data = select_user(1)
    '''
    data_dict = {
                     "id_user": data[0],
                     "name": data[1],
                     "gender": data[2],
                     "dt_birth": (data[3]).strftime("%x"),
                     "cep": data[4],
                     "street": data[5],
                     "complement": data[6],
                     "neighborhood": data[7],
                     "city": data[8],
                     "state": data[9]
                }
    y = json.dumps(data_dict)

    #print(type(data_dict))

   
    payload = {"id_user": 1,
               "name": "Renata",
               "gender": "F",
               "dt_birth": "2001-05-02",
               "cep": "03637000",
               "street": "Rua da Graça",
               "complement": "APTO 10",
               "neighborhood": "Centro",
               "city": "São Paulo",
               "state": "SP"}

    insert_user(payload)
    '''
