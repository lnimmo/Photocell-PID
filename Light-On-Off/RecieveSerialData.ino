#include <PID_v1.h>

double Setpoint; //PID setpoint
double photocellReading; //input
double ledBrightness; //output

double kp = .1, ki = 10, kd = .012;

#define photocellPin 0
#define ledPin 5

//setup the PID
PID myPID(&photocellReading, &ledBrightness, &Setpoint, kp, ki, kd, DIRECT);


void setup() {
  Serial.begin(9600);
  Serial.println("python connected");
  Setpoint = 600;
  myPID.SetMode(AUTOMATIC);
  myPID.SetTunings(kp, ki, kd);
}

void loop() {
  if (Serial.available()) {
    int pythonSerialData = Serial.read();
    if (pythonSerialData == '1') {
      analogWrite(ledPin, 100);
      Serial.println("data recieved");
    } else if (pythonSerialData == '0') {
      analogWrite(ledPin, 0);
      Serial.println("data recieved");
    }
  }
}
