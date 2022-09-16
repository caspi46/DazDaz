import sqlite3
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import threading
from sklearn.linear_model import LinearRegression
import pandas as pd
from pylab import *
from collections import namedtuple

condition = threading.Condition()

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
class sqlite:
    def __init__(self):
        self.afile = "DAZDAZ.db"

    def connect(self):
        try:
            sqliteConnection = sqlite3.connect(self.afile)
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def table(self, name):
        try:
            sqliteConnection = sqlite3.connect(self.afile)
            if name == "Database":
                sqlite_create_table_query = '''CREATE TABLE Database(
                                                      ID INTEGER PRIMARY KEY,
                                                      TITLE TEXT NOT NULL,
                                                      VIEW INTEGER NOT NULL,
                                                      DATE TEXT NOT NULL,
                                                      Link TEXT NOT NULL);'''
                # LIKE INTEGER PRIMARY KEY,

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

    def insert(self, id, title, view, date, link):
        condition.acquire()
        try:
            sqliteConnection = sqlite3.connect(self.afile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_blob_query = """INSERT INTO Database
                                        (ID, TITLE, VIEW, DATE, LINK)
                                        VALUES (?, ?, ?, ?, ?)"""
            data_tuple = (id, title, view, date, link)

            cursor.execute(sqlite_insert_blob_query, data_tuple)
            sqliteConnection.commit()
            print("File inserted successfully as a BLOB into a table")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The sqlite connection is closed")
        condition.release()
