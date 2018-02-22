import RPi.GPIO as gpio
import time
import requests.packages.urllib3
import requests
import json
# from firebase import firebase

gpio.setwarnings(False)

ledPin1 = 12
ledPin2 = 13
echoPin1 = 22
echoPin2 = 16
trigPin1 = 18
trigPin2 = 15

counter = 0
dirValue1 = 'parkSense1/value'
dirValue2 = 'parkSense2/value'
dirValueChanger = 'status/value'

# firebase_url = 'https://resplendent-heat-8054.firebaseio.com'
# firebase = firebase.FirebaseApplication('https://resplendent-heat-8054.firebaseio.com', None)
# auth_token = 'RRgoYFKBnOXIejFKAaTHxuqjCZWB3ARZi6MeHGpa'

# requests.packages.urllib3.disable_warnings()
gpio.setmode(gpio.BOARD)
gpio.setup(ledPin1, gpio.OUT)
gpio.setup(ledPin2, gpio.OUT)
gpio.setup(echoPin1, gpio.IN)
gpio.setup(echoPin2, gpio.IN)
gpio.setup(trigPin1, gpio.OUT)
gpio.setup(trigPin2, gpio.OUT)

gpio.output(trigPin1, False)
gpio.output(trigPin2, False)
time.sleep(2)

try:
    while True:
    	request = firebase.get('/status', 'value')
		result = int(request)
        print result
        print counter
        
        status_ldr1 = gpio.output(ldrPin1_1)
        status_ldr2 = gpio.output(ldrPin1_2)
        status_ldr3 = gpio.output(ldrPin2_1)
        status_ldr4 = gpio.output(ldrPin2_2)

        if (status_ldr1==1) or (status_ldr2==1)
            # Lantai 1 Code // Slot 1
            if (status_ldr1==1): #LDR Slot 1 Mendeteksi
                if (counterActive==0) #Jika program baru dimulai


        if (result==1): 
            status_ldr = gpio.input(ldrPin1_1)
            if (status_ldr==1):
                gpio.output(trigPin1, True)
                time.sleep(0.00001)
                gpio.output(trigPin1, False)

                while gpio.input(echoPin1)==0:
                    pulse_start1 = time.time()

                while gpio.input(echoPin1)==1:
                    pulse_end1 = time.time()

                pulse_duration1 = pulse_end1 - pulse_start1
                distance1 = pulse_duration1 * 17150
                distance1 = round(distance1, 2)

                if (distance1<=5):
                    print 'SLOT 1 Lantai 1 : Penuh gan!, ' + str(distance1)
                    gpio.output(ledPin1, gpio.LOW)
                else:
                    print 'SLOT 1 Lantai 1 : Kosong gan!, ' + str(distance1)
                    gpio.output(ledPin1, gpio.HIGH)

                sensorValue1 = gpio.input(ledPin1)
                result1 = requests.put(firebase_url + '/' + dirValue1 + '/.json' + '?auth=' + auth_token, data=json.dumps(sensorValue1))
                #print 'Record inserted. Result Code = ' + str(result.status_code)

                slotCondition == True
            
        elif (result==2):
            gpio.output(trigPin2, True)
            time.sleep(0.00001)
            gpio.output(trigPin2, False)

            while gpio.input(echoPin2)==0:
                pulse_start2 = time.time()

            while gpio.input(echoPin2)==1:
                pulse_end2 = time.time()

            pulse_duration2 = pulse_end2 - pulse_start2
            distance2 = pulse_duration2 * 17150
            distance2 = round(distance2, 2)

            if (distance2<=5):
                print 'SLOT 2 : Penuh gan!, ' + str(distance2)
                gpio.output(ledPin2, gpio.HIGH)
            else:
                print 'SLOT 2 : Kosong gan!, ' + str(distance2)
                gpio.output(ledPin2, gpio.LOW)

            sensorValue2 = gpio.input(ledPin2)
            result2 = requests.put(firebase_url + '/' + dirValue2 + '/.json' + '?auth=' + auth_token, data=json.dumps(sensorValue2))
            #print 'Record inserted. Result Code = ' + str(result.status_code)
        else:
            print 'Missing Error'

        if (counter==10):
            changeValue = 2
            resultChanger = requests.put(firebase_url + '/' + dirValueChanger + '/.json' + '?auth=' + auth_token, data=json.dumps(changeValue))

        # time.sleep(3)
        counter = counter + 1

except KeyboardInterrupt:
        print 'Operation has been canceled'
        gpio.cleanup()