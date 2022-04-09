from sense_hat import SenseHat
sense = SenseHat() 

def prime_pressure():
  t_pressure = sense.get_temperature_from_pressure()
  print({"t_pressure": t_pressure})

if __name__ == '__main__':
    prime_pressure()

