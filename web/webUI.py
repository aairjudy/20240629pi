import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh
load_dotenv()
st_autorefresh()
# redis_conn =redis.Redis(host = os.environ['REDIS_HOST'],port=6379,password=os.environ['REDIS_PASSWORD'])
redis_conn = redis.from_url( url = os.environ['RENDER_REDIS_INTERNAL'])
bytes_list = redis_conn.lrange("501教室/德順",-5,-1)

str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list) ]
dict_list = [json.loads(string) for string in str_list]
df1 = pd.DataFrame(dict_list)
# print (dict_list)


st.dataframe(df1,hide_index=True, column_config={
                 "status":st.column_config.CheckboxColumn(label='按鈕狀態',width='small'),
                 "data":st.column_config.DatetimeColumn(label='時間',width='medium'),
                 "topic":st.column_config.TextColumn(label='主題',width='large')
             })
# st.write(dict_list)
st.title('訓練不通教室')
st.header('這是Header:bule[cool]:sunglasses:')
# print (str_list)