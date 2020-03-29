from repository import user_repository


def create_user(payload):
    user_repository.insert_user(payload)
