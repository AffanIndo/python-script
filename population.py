import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()


cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
con.commit()

cur.execute('SELECT Region, Population FROM PopByRegion')
print(cur.fetchall())