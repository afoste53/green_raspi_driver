from constants import T_HEAT_OFF, TMAX, TMIN, STRIP_HOST, PLUG_MAPPING, HEAT_URL
from kasa import SmartStrip
import asyncio
import requests

async def screen_temp(temp):
    try:

        strip = SmartStrip(STRIP_HOST)
        await strip.update()        

        heater = strip.children[PLUG_MAPPING["heater"]]

        if temp < TMIN:
            # turn things on
            if not heater.is_on:
                await heater.turn_on()
            else:
                send_notification({"message": "Too Cold!", "Temp": temp}) 
        elif temp > T_HEAT_OFF:
            # turn things off
            if heater.is_on:
                await heater.turn_off()

        if temp > TMAX:
            # alert me
            send_notification({"message": "Too Hot!", "Temp": temp})

        await strip.update()

    except Exception as err:
        handle_err(err)
     
    return 

def send_notification(notification):
    req = requests.post(url = HEAT_URL,  data = notification)
    if req.status_code != 200:
        print(f"Error occured when trying to send notification with notification {notification}")

    return req

def handle_err(err):
    print(f"Something has gone terribly wrong: {err}")     


if __name__ == '__main__':
    asyncio.run(screen_temp(40.0))
