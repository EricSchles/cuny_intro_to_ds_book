import sqlite3 as sql
import pandas as pd

df = pd.read_csv("economy.csv")

connection = sql.connect("economy.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE industry (
       id int,
       manufacturing float,
       technology float,
       real_estate float
)
""")
for index, row in df.iterrows():
    cursor.execute(f"""
    INSERT INTO industry (
       'id',
       'manufacturing',
       'technology',
       'real_estate'
    ) VALUES (
    {index}, {row["Manufacturing"]},
    {row["Technology"]}, {row["Real Estate"]}
    )
    """)
connection.commit()
connection.close()
