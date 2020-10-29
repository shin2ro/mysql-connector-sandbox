from mysql.connector import connect


if __name__ == '__main__':
    with connect(host='192.168.33.10', user='user', password='password') as conn:
        print('Connection Successful.')
