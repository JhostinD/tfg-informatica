# Functions that will prepare the connection (cursor) to postgreSQL
from pandas import DataFrame
from psycopg2 import connection

def insert_sql(sql: str, df: DataFrame, conn: connection):
    # Cursor from connection to execute query
    with conn.cursor() as cursor:
        # Iterating through each row from DataFrame and inserting them into database
        for index, row in df.iterrows():
            cursor.execute(sql, tuple(row))

    # Saving changes in database
    conn.commit()