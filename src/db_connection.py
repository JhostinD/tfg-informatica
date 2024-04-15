# Functions that will prepare the connection (cursor) to postgreSQL
from cfg import DB_PASS, DB_USER, DB_NAME, DB_HOST
from sqlalchemy import create_engine
import psycopg2

# sqlalchemy engine setup for a postgresql database
conn_string = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
database = create_engine(conn_string)
conn_sql_alchemy = database.connect()

# Connection to database
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS)


def insert_rows(df, table_name, schema_name):
    """
    Insert rows from a Pandas DataFrame into a PostgreSQL table.

    Parameters:
    - df: Pandas DataFrame containing the data to be inserted.
    - table_name: Name of the PostgreSQL table to insert the data into.
    - schema_name: Name of the PostgreSQL schema to insert the data into.

    Note: Assumes that the table columns match the DataFrame columns.
    """
    try:
        # Open a cursor to perform database operations
        cursor = conn.cursor()

        # Insert DataFrame values into sql table via sqlAlchemy
        # Note: In case of PK conflict replaces the old row
        df.to_sql(table_name, conn_sql_alchemy, if_exists='replace')

        # Commit the changes
        conn.commit()

    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close the cursor
        cursor.close()
