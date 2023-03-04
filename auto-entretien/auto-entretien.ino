#include <Servo.h>

const int capteurPin = 13;
const int accordServoPin = 9;
const int harmo1ServoPin = 3;
const int harmo2ServoPin = 4;

float desiredFrequency = 105;

bool servo1Up = true;

Servo accordServo;
Servo harmo1Servo;
Servo harmo2Servo;

int accordPos = 90;

void setup() {
  pinMode(capteurPin, INPUT);
  pinMode(5, INPUT);
  accordServo.attach(accordServoPin);
  harmo1Servo.attach(harmo1ServoPin);
  harmo2Servo.attach(harmo2ServoPin);
  Serial.begin(57600);
  delay(1000);
  harmo1Servo.write(5);
  harmo2Servo.write(90);
  accordServo.write(accordPos);
  delay(1000);
}

void loop() {
    float frequency = calculateFrequency();
    Serial.println(frequency);
    autoEntretien(frequency);
    while (calculateFrequency() < desiredFrequency - 1.){
        autoEntretien(frequency);
        accordPos += 1;
        accordServo.write(accordPos);
        delay(100);
    }
    while (calculateFrequency() > desiredFrequency + 1.){
        autoEntretien(frequency);
        accordPos -= 1;
        accordServo.write(accordPos);
        delay(100);
    }
    delay(1000);
}

// ===========================================================
// Fonctions =================================================
// ===========================================================

void autoEntretien(float frequency) {
    if (digitalRead(5)){
        harmo2Servo.write(111);
    } else {
      harmo2Servo.write(90);
    }
    while (isinf(frequency) || frequency == 0){
        // Serial.println(frequency);
        if (servo1Up){
          harmo1Servo.write(85);
          servo1Up = false;
        } else {
          harmo1Servo.write(5);
          servo1Up = true;
        }
        frequency = calculateFrequency();
        delay(200);
    }
}

float calculateFrequency() {
    int pulseHigh = pulseIn(capteurPin, HIGH);
    int pulseLow = pulseIn(capteurPin, LOW);
    float pulseTotal = pulseHigh + pulseLow; // Time period of the pulse in microseconds
    float count = 1000000 / pulseTotal;
    if (digitalRead(5)){
        count = count/2;
    }
    return count;
}