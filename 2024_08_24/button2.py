
import signal
from gpiozero import Button,LED
from datetime import datetime
import os
from dotenv import load_dotenv
# import paho.mqtt.publish as publish
from  paho.mqtt import publish
load_dotenv()

def user_release():
    print("使用者按下放開")
    led.toggle()
    now = datetime.now()
    now_str = now.strftime('%y-%m-%d %H:%M:%S')

    print(now_str)
    msgs = [{'topic':"paho/test/topic", 'payload':"multiple 1"},
    ("paho/test/topic", "multiple 2", 0, False)]
    now = datetime.now()
    strnow = now.strftime('%y%m%d %H:%M:%S')
    if led.is_lit:
        message = f'''{{
        "status":"true",
        "data":"{now_str}",
        "topic":"501教室/德順"
        }}'''         # message = '燈是開的'
        print(message)
        publish.single(topic='501教室/德順',payload=message,hostname='127.0.0.1',qos = 2,auth={'username':os.environ['MQTT_USERNAME'],'password':os.environ['MQTT_PASSWORD']})
    else:        
        message = f'''{{
        "status":"false",
        "data":"{now_str}",
        "topic":"501教室/德順"
        }}''' #'燈是關的'
        print(message)
        publish.single(topic='501教室/德順',payload=message,hostname='127.0.0.1',qos = 2,auth={'username':os.environ['MQTT_USERNAME'],'password':os.environ['MQTT_PASSWORD']})
if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25) 
    signal.pause()
