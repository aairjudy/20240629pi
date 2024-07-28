import os,os.path
from datetime import datetime as sdate
import random

dirPath = os.path.abspath(__name__)
dictName = os.path.dirname(dirPath)
extPath = os.path.join(dictName,"extent")
if os.path.isdir(extPath):
    print ('有資料夾:'+extPath)
else:
    os.makedirs(extPath)
    print ('建立資料夾:'+extPath)

filepath = os.path.join(extPath,"runing.log")
print (filepath)
if os.path.isfile(filepath):
    print ('有檔案')
else:
    print('沒有檔案') 
    with open(filepath,'w',encoding='utf-8',newline = '\n') as file:
        file.write('日期,溫度,濕度\n')
   

dt = sdate.now()
strdt =dt.strftime('%Y-%m-%d %H:%M:%S')

temp =  str(random.randint(50,300)/10)
wet =  str(random.randint(200,800)/10)
print (temp,wet)
with open(filepath,'a',encoding='utf-8',newline='\n') as file:
    file.write (strdt +","+ wet + "%" + "," + temp +"\n")
