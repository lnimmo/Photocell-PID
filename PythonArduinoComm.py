import serial
import time


mySerial = serial.Serial('COM6', 9600,)
serialReadData = mySerial.readline().decode('ascii')
print(serialReadData)
print("enter 1 for light on")
print("enter 2 for light off")
print("enter 3 for quit")

def pullDataFromArduino():
    startTime = time.time()
    timePeriod = 5
    while True:
        print(mySerial.readline().decode('ascii'))
        if time.time() > startTime + timePeriod : break
    mySerial.write('0'.encode())
    requestUserInput()
    
def requestUserInput():
    runTest = False
    while runTest == False :
        inputData = input('enter a number: ')
        print(inputData)
    
        if (inputData == '1'):
            mySerial.write(inputData.encode())
            print('light on?')
            pullDataFromArduino()
            runTest = True

        if (inputData == '0'):
            mySerial.write(inputData.encode())
            print('light off?')

        if (inputData == '3'):
            mySerial.write('0'.encode())
            mySerial.close()
            quit()

requestUserInput()