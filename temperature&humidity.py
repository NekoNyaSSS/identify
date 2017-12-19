# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
print "“Pleace Waite........"
while 1==1:
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)    #设定使用物理针脚编号
    time.sleep(1)
    pin=40                                        #规定DHT11的DATA接在树莓派物理40针
    data=[]
    def delay(i): #20*i usdelay
        a=0
        for j in range(i):
            a+1
    j=0
    #start work
    gpio.setup(pin,gpio.OUT)
    gpio.output(pin,gpio.LOW)
    time.sleep(0.02)
    gpio.output(pin,gpio.HIGH)
    i=1
    #wait to response
    gpio.setup(pin,gpio.IN)
    while gpio.input(pin)==1:
        continue
    while gpio.input(pin)==0:
        continue
    while gpio.input(pin)==1:
        continue
    #get data
    while j<40:
        k=0
        while gpio.input(pin)==0:
            continue
        while gpio.input(pin)==1:
            k+=1
            if k>100:break
        if k<3:
            data.append(0)
        else:
            data.append(1)
        j+=1
 
    #get temperature
    humidity_bit=data[0:8]
    humidity_point_bit=data[8:16]
    temperature_bit=data[16:24]
    temperature_point_bit=data[24:32]
    check_bit=data[32:40]
    humidity=0
    humidity_point=0
    temperature=0
    temperature_point=0
    check=0
    for i in range(8): 
        humidity+=humidity_bit[i]*2**(7-i)
        humidity_point+=humidity_point_bit[i]*2**(7-i)
        temperature+=temperature_bit[i]*2**(7-i)
        temperature_point+=temperature_point_bit[i]*2**(7-i)
        check+=check_bit[i]*2**(7-i)
    #输出结果 
    tmp=humidity+humidity_point+temperature+temperature_point
    if check==tmp:
        print "temp: ", temperature,"C"
        print "wet : ",humidity,"%"
        break
    else:
        continue
        print "something is worong"

