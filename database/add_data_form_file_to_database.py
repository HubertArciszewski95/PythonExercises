# Add data form file to database
import sqlite3
import pandas

data = pandas.read_csv("/Users/hubertarciszewski/Downloads/ten-more-countries.txt")


conn = sqlite3.connect("/Users/hubertarciszewski/Downloads/database.db")
cur = conn.cursor()

for index, row in data.iterrows():
    cur.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)", (row["Country", row["Area"]]))
conn.commit()
conn.close()


