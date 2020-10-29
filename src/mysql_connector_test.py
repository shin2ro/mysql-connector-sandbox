from argparse import ArgumentParser

from mysql.connector import connect


def connect_db(host, user, password):
    with connect(host=host, user=user, password=password) as conn:
        print('Connection Successful.')



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('host')

    args = parser.parse_args()

    connect_db(args.host, 'user', 'password')

