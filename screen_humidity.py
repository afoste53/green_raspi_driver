from constants import HMAX, HMIN, TMAX, TMIN, T_HEAT_OFF, HUM_URL, PLUG_MAPPING, STRIP_HOST
from kasa import SmartStrip
import requests
import asyncio

async def screen_humidity(hum, temp):
    try:
        strip = SmartStrip(STRIP_HOST)
        await strip.update()

        humidifier = strip.children[PLUG_MAPPING["humidifier"]]

        if hum <= HMIN:
            # turn on humidity
            if temp <= T_HEAT_OFF and not humidifier.is_on:
                await humidifier.turn_on()
            else:
                send_notification({"message": "Not humid enough!", "humidity": hum, "temp": temp})
        elif hum >= HMAX:
            # turn off
            if humidifier.is_on:
                await humidifier.turn_off()
            else:
                send_notification({"message": "Too humid!", "humidity": hum, "temp": temp})    

    except Exception as err:
        handle_err(err)     

    await strip.update()

def send_notification(notification):
    req = requests.post(url = HUM_URL, data = notification)
    if req.status_code != 200:
        print(f"Error occurred while trying to send a notification: {notification}")

    return req

def handle_err(err):
    print(f"Something has gone terribly wrong: {err}")     


if __name__ == '__main__':
    asyncio.run(screen_humidity(97.0, 9.0))


