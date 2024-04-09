

import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="otraclase"
        )
    except mysql.connector.Error as err:
        raise err


