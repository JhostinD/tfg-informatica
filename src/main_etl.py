from cfg import DB_PASS, DB_USER, DB_NAME, DB_HOST, DB_PORT#, NASDAQ_TOKEN
from google.cloud import bigquery
import db_connection as db
import nasdaqdatalink as nd
import pandas as pd
import numpy as np
import psycopg2 as psy

# Google Cloud BigQuery client for extracting raw data
client = bigquery.Client()

def extract():
    query = "SELECT * FROM `housecanary-com.sample.zip_ts` LIMIT 50"

    query_job = client.query(query)

    return query_job


def transform(data_raw):
    '''
    columns that will be saved (from 'zip_ts' table from dataset ):
        - zip (string): 5 digit postal code
        - month (date): timeseries date
        - hpi_value (float): nominal housing price index
        - hpi_real (float): real housing price index after adjusting nominal hpi for inflation as measured by the CPI
    '''

    # Selecting desired columns and saving them in a list for filtering next
    selected_columns = ['zip', 'msa', 'month', 'hpi_value', 'hpi_real']

    # Getting DataFrame from previous query result
    df_clean = data_raw.to_dataframe()

    # Filtering columns given selected columns list
    df_clean = df_clean.loc[:, selected_columns]

    return df_clean


def load(conn, df):
    # Table and Schema
    table_name = "zip_ts_raw"
    schema_name = "public"
    
    db.insert_rows(df, table_name, schema_name, conn)


if __name__ == "__main__":

    # Retrieving raw data from Google Cloud Platform dataset (House-canary)
    data_raw = extract()

    # Transforming raw data into processed data for database
    data_processed = transform(data_raw)

    # Connection to database
    conn = psy.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT, host=DB_HOST)

    # Loading processed data into database
    load(conn, data_processed)

    # Closing database connection
    conn.close()
