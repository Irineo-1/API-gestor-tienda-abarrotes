# import mysql.connector
# import os
# from dotenv import load_dotenv
import sqlite3

# load_dotenv()

# def getConexion():
#     mydb = mysql.connector.connect(
#     host=os.getenv("HOST"),
#     user=os.getenv("USER"),
#     password=os.getenv("PASSWORD"),
#     database=os.getenv("DATABASE")
#     )
#     return mydb

def getConexion():
    conn = sqlite3.connect("models/db/punto_venta.db")
    conn.row_factory = sqlite3.Row
    return conn