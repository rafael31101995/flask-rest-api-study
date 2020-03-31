from repository import user_repository


def create_user(payload):
    user_repository.insert_user(payload)


def select_all_users():
    user_repository.select_all_users()


def select_user(id_user):
    return user_repository.select_user(id_user)


if __name__ == "__main__":
    select_user(1)