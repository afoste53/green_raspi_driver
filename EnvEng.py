from sense_hat import SenseHat
import time
import datetime
from concurrent import futures
import sqlite3
from screen_humidity import screen_humidity
from screen_temp import screen_temp
import asyncio

sense = SenseHat() 

con = sqlite3.connect('./grow_one.db')
cur = con.cursor()


def store_vals():
  t_pressure = round(sense.get_temperature_from_pressure(),3)
  t_humidity = round(sense.get_temperature_from_humidity(),3)
  humidity = round(sense.get_humidity(),3)
  date = datetime.datetime.now()

  cur.execute("INSERT INTO t_pressure(date, val) VALUES(?,?)", (date, t_pressure))
  cur.execute("INSERT INTO t_humidity(date, val) VALUES(?,?)", (date, t_humidity))
  
  asyncio.run(screen_temp(t_humidity))

  asyncio.run(screen_humidity(humidity, t_humidity))
  cur.execute("INSERT INTO humidity(date, val) VALUES(?,?)", (date, humidity))
  
  con.commit()

  print( {"t_pressure": t_pressure, "t_humidity":t_humidity,"humidity":humidity})

if __name__ == '__main__':
  while(True):
    store_vals()
    time.sleep(600)  

