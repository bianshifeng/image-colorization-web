''' seed "users" collection '''

from werkzeug.security import generate_password_hash
from server.utils.mongo import mongo


def users_seed():
    # get collection
    collection = mongo['users']

    # indexes
    collection.create_index('username', unique=True)

    # data
    users = []
    for i in range(10):
        users.append({
            'username': 'dummy{}'.format(i),
            'hashed_password': generate_password_hash('dummy{}'.format(i)),
            'display_name': 'Dummy #{}'.format(i),
            'authority': 4
        })

    collection.insert_many(users)
