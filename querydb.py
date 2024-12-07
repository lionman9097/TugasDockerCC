import sqlite3
import pandas as pd

con= sqlite3.connect("data.db")
print(pd.read_sql_query("SELECT * FROM users",con))
con.close()