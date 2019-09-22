import serial
import time

mySerial = serial.Serial('COM6', 9600,)
print(mySerial.readline().decode('ascii'))
print("enter 1 for light on")
print("enter 2 for light off")
print("enter 3 for quit")

while 1:
    inputData = input('enter a number: ')
    print(inputData)

    if (inputData == '1'):
        mySerial.write(inputData.encode())
        print('light on?')

    if (inputData == '0'):
        mySerial.write(inputData.encode())
        print('light off?')

    if (inputData == '3'):
        mySerial.write('0'.encode())
        mySerial.close()
        quit()


