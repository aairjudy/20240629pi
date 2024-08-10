import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    print("使用者按下放開" ,end = '\t')
    led.toggle()
    now = datetime.now()
    strNow =now.strftime('%Y-%m-%d %H:%M:%S')
    print (strNow ,end = '\t')

    if led.is_lit:
        print ('開啟電燈中')
    else:
        print ('電燈已關閉')

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release 
    led =LED(pin=25)


    signal.pause()