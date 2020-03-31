import pymysql


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
    print(user)
    return user


def format_query(json):
    return "INSERT INTO user (id_user, name, gender, dt_birth, cep, street, complement, neighborhood, city, " \
           "state) VALUES " \
           "({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
        json['id_user'], json['name'], json['gender'], json['dt_birth'], json['cep'], json['street'],
        json['complement'], json['neighborhood'], json['city'], json['state'])


def connect_to_mysql(host, username, password, database):
    return pymysql.connect(host, username, password, database)


if __name__ == "__main__":
    select_user(1)
    '''
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