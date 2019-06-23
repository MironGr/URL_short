import sqlite3 as lite
import sys


def query_save_db(query_str):

    try:
        conn = lite.connect('URL_short_serv_1.db')
        cursor = conn.cursor()
        cursor.execute(query_str)
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if conn:
            conn.close()
    # with open("data_file.txt", "r+") as write_file:
    #     json.dump(data, write_file)


def query_db(query_str):

    try:
        conn = lite.connect('URL_short_serv_1.db')
        cursor = conn.cursor()
        cursor.execute(query_str)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if conn:
            conn.close()
