import sqlite3

con = sqlite3.connect('myb1')

sth = con.cursor()

sth.execute("select * from t1")
print(sth.fetchone())
con.commit()

con.close()