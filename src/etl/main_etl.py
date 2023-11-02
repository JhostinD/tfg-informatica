from cfg import DB_PASS, DB_USER, DB_NAME
import db.db_connection as db
import nasdaqdatalink as nd
import pandas as pd
import numpy as np
import psycopg2 as psy

def extract():
    pass


def transform(data_raw):
    pass


def load(conn, df):
    # Query
    sql_insert = """
                 INSERT INTO public.recent_played_tracks(
                 album_name, song_name, album_image, played_at)
                 VALUES (%s, %s, %s, %s);
                 """
    db.insert_sql(sql_insert, df, conn)


if __name__ == "__main__":

    # Retrieving raw data from nasdaq API
    data_raw = extract()

    # Transforming raw data into processed data for database
    data_processed = transform(data_raw)

    # Connection to database
    conn = psy.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS)

    # Loading processed data into database
    load(conn, data_processed)

    # Closing database connection
    conn.close()
