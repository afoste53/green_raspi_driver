import sqlite3

# connect and set up cursor
con = sqlite3.connect('./grow_one.db')
cur = con.cursor()

# create t_pressure table
cur.execute('''CREATE TABLE t_pressure
		(date text, val real)''')

# create t_humidity table
cur.execute('''CREATE TABLE t_humidity
		(date text, val real)''')

# create humidity table
cur.execute('''CREATE TABLE humidity
		(date text, val real)''')

"""
# create ph table
cur.execute('''CREATE TABLE ph
		(date text, val real)''')
"""
# save and close connection
con.commit()
con.close()
