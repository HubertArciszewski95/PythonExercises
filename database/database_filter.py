# print form file database.db those countries that have area grater than 2m
import sqlite3

conn = sqlite3.connect("/Users/hubertarciszewski/Downloads/database.db")
c = conn.cursor()

c.execute("SELECT country FROM countries WHERE area >= 2000000")
x = c.fetchall()
conn.close()

for i in x:
    print(i[0])
