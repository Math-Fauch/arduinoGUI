#include <Servo.h>

const int capteurPin = 13;
const int accordServoPin = 9;
const int harmo1ServoPin = 3;
const int harmo2ServoPin = 4;

int accordServoPos = 90;

float desiredFrequency = 105.;

bool servo1Up = true;
bool servo2Up = false;

Servo accordServo;
Servo harmo1Servo;
Servo harmo2Servo;

void setup() {
    pinInit();
    Serial.begin(57600);
    delay(1000);
    servoPosInit();
    delay(1000);
}

void loop() {
    autoEntretien();
    if (!isinf(calculateFrequency())){
        while (calculateFrequency() < desiredFrequency - 1.){
            autoEntretien();
            accordServoPos += 1;
            accordServo.write(accordServoPos);
            delay(100);
        }
        while (calculateFrequency() > desiredFrequency + 1.){
            autoEntretien();
            accordServoPos -= 1;
            accordServo.write(accordServoPos);
            delay(100);
        }
    }
    delay(1000);
}

// ===========================================================
// Fonctions =================================================
// ===========================================================

void autoEntretien() {
    float frequency = calculateFrequency();
    while (isinf(frequency) || frequency == 0){
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
    return count;
}

void changeHarmonic(){
    if (harmo2ServoUp){
        harmo2Servo.write(90);
        harmo2ServoUp = false;
    } else {
        harmo2Servo.write(111);
        harmo2ServoUp = true;
    }
}

float getDesiredFrequency() {
  if (Serial.available() > 0) {
    float myFloat = Serial.parseFloat(SKIP_ALL, '\n');
    Serial.print("a")
  }
}

// // // // // // // // // // // // 
// FONCTIONS INITIALISATION   // // 
// // // // // // // // // // // // 

void pinInit(){
    pinMode(capteurPin, INPUT);
    accordServo.attach(accordServoPin);
    harmo1Servo.attach(harmo1ServoPin);
    harmo2Servo.attach(harmo2ServoPin);
}

void servoPosInit(){
    harmo1Servo.write(5);
    harmo2Servo.write(90);
    accordServo.write(accordServoPos);
}


/*
a = fréquence désiré reçue par l'Arduino
b = auto-entretien obtenu
c = auto-accord abtenu
*/