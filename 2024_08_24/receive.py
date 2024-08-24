import paho.mqtt.client as mqtt
import redis
import os
from dotenv import load_dotenv
import json
from tools import created_log_file,record_info
from datetime import datetime
load_dotenv()

#redis_conn =redis.Redis(host = '172.16.1.37',port=6379,password='xxxx')
redis_conn =redis.Redis(host = os.environ['REDIS_HOST'],port=6379,password=os.environ['REDIS_PASSWORD'])
render_redis_conn = redis.Redis.from_url(os.environ['RENDER_REDIS'])

print(redis_conn.ping())

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    render_redis_conn.rpush(topic,message)
    # print(f"topic={topic},message:{message}")
    message_dict = json.loads(s=memoryview)
    print (message_dict)

if __name__ == '__main__':
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    client.username_pw_set(username=os.environ['MQTT_USERNAME'],password=os.environ['MQTT_PASSWORD'])
    client.on_message = on_message
    client.connect( os.environ['MQTT_SERVER'])
    client.subscribe('501教室/德順',qos=2)
    client.loop_forever()