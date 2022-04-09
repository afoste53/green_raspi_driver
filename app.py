from sense_hat import SenseHat
import time
from concurrent import futures
from flask import Flask, json
from flask_cors import CORS
import sqlite3

sense = SenseHat() 

api = Flask(__name__)
CORS(api)

con = sqlite3.connect('./grow_one.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

# route to fetch all vals from db
# TODO: execute this as batches?
@api.route('/', methods=['GET'])
def get_vals():
  t_pressure = cur.execute("SELECT * FROM t_pressure").fetchall()
  t_humidity = cur.execute("SELECT * FROM t_humidity").fetchall()
  humidity = cur.execute("SELECT * FROM humidity").fetchall() 

  vals ={"t_pressure": t_pressure, "t_humidity": t_humidity, "humidity": humidity}
  return vals

# route to fetch current values
@api.route('/currently', methods=['GET'])
def get_current():
  t_pressure = sense.get_temperature_from_pressure()
  t_humidty = sense.get_temperture_from_humidity()
  humidity = sense.get_humidity()

  vals ={"t_pressure": t_pressure, "t_humidity": t_humidity, "humidity": humidity}
  return vals

if __name__ == '__main__':
    api.run()

