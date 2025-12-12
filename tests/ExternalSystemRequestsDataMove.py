# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import urllib

# =================CONFIGURATION=================
# MySQL Details
MYSQL_USER = 'idmread'
MYSQL_PASS = urllib.parse.quote('***********')
MYSQL_HOST = 'rmy107tst.csfbgpprhbve.us-east-1.rds.amazonaws.com'
MYSQL_PORT = '3306'
MYSQL_DB   = 'idmCSharp'

# MSSQL Details
MSSQL_SERVER = 'bergen.bilh.itsystems.org'  # e.g., localhost\SQLEXPRESS or IP
MSSQL_DB     = 'IDM3'
MSSQL_USER   = 'idmuser'
MSSQL_PASS   = '******************'
# Driver: Check your ODBC Data Sources (usually ODBC Driver 17 or 18 for SQL Server)
MSSQL_DRIVER = 'ODBC Driver 17 for SQL Server'

MYSQL_TABLE_NAME   = 'external_system_requests'
MSSQL_TABLE_NAME = 'external_system_requests_old'
# ===============================================

try:
    # 1. Create MySQL Engine
    mysql_conn_str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    mysql_engine = create_engine(mysql_conn_str)

    # 2. Create MSSQL Engine
    # SQLAlchemy requires a specific URL format for PyODBC
    params = urllib.parse.quote_plus(
        f"DRIVER={{{MSSQL_DRIVER}}};SERVER={MSSQL_SERVER};DATABASE={MSSQL_DB};UID={MSSQL_USER};PWD={MSSQL_PASS}"
    )
    mssql_conn_str = f"mssql+pyodbc:///?odbc_connect={params}"
    mssql_engine = create_engine(mssql_conn_str)

    print("Reading from MySQL...")
    # Read data
    df = pd.read_sql(f"SELECT * FROM {MYSQL_TABLE_NAME} WHERE ID > 100000000 AND ID <= 200000000", mysql_engine)

    print(f"Read {len(df)} rows. Writing to MSSQL...")

    # Write data
    # if_exists options: 'fail', 'replace', 'append'
    # chunksize: writes rows in batches (good for memory)
    df.to_sql(MSSQL_TABLE_NAME, mssql_engine, if_exists='append', index=False, chunksize=1000)

    print("Transfer Complete.")

except Exception as e:
    print(f"Error: {e}")