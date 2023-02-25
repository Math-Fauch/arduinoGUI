#include <Servo.h>

Servo myservo;  // create servo object to control a servo
const int ledPin = 13;  // the pin that the LED is attached to
const int servoPin = 9;  // the pin that the LED is attached to
int incomingByte;       // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
    // if it's a lowercase f (ASCII 72), put the servo to 5 degree:
    if (incomingByte == 'f') {
      myservo.write(5);              // tell servo to go to position 5
      Serial.println(5);
    }
    // if it's a capital F (ASCII 72), put the servo to 170 degree:
    if (incomingByte == 'F') {
      myservo.write(170);              // tell servo to go to position 170
      Serial.println(170);
    }
  }
}