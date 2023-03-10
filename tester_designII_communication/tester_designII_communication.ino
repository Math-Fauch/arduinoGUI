// // #include <Servo.h>

// // Servo myservo;  // create servo object to control a servo
const int ledPin = 13;  // the pin that the LED is attached to
// // const int servoPin = 9;  // the pin that the LED is attached to
// int incomingByte;       // a variable to read incoming serial data into
// float test = 100.;
// byte test1[100];

// void setup() {
//   // initialize serial communication:
//   Serial.begin(9600);
//   // initialize the LED pin as an output:
//   pinMode(ledPin, OUTPUT);
//   // myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object
// }

// void loop() {
//   // see if there's incoming serial data:
//   if (Serial.available() > 0) {
//     // read the oldest byte in the serial buffer:
//     // incomingByte = Serial.readBytesUntil('\n', test1, 100);
//     float myFloat = Serial.parseFloat(SKIP_ALL, '\n');
//     // if it's a capital H (ASCII 72), turn on the LED:
//     if (myFloat == test) {
//       digitalWrite(ledPin, HIGH);
//     }
//     // if it's an L (ASCII 76) turn off the LED:
//     if (myFloat != test) {
//       digitalWrite(ledPin, LOW);
//     }
//     // // if it's a lowercase f (ASCII 72), put the servo to 5 degree:
//     // if (incomingByte == 'f') {
//     //   myservo.write(5);              // tell servo to go to position 5
//     //   Serial.println(5);
//     // }
//     // // if it's a capital F (ASCII 72), put the servo to 170 degree:
//     // if (incomingByte == 'F') {
//     //   myservo.write(170);              // tell servo to go to position 170
//     //   Serial.println(170);
//     // }
//   }
// }




bool ledOn = false;
int x = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (x < 10){
    x += 1;
    delay(500);
  } else {
    if (Serial.available() > 0) {
      float myFloat = Serial.parseFloat(SKIP_ALL, '\n');

      if (myFloat == 100.){
        digitalWrite(ledPin, LOW);
        ledOn = false;
      } else {
        digitalWrite(ledPin, HIGH);
        ledOn = true;
      }
      Serial.println("o");
    }
    x = 0;
  }
}