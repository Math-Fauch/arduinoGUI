const int capteurPin = 13;
const int actionneurPin = 9;
int pulseHigh; // Integer variable to capture High time of the incoming pulse
int pulseLow; // Integer variable to capture Low time of the incoming pulse
float pulseTotal; // Float variable to capture Total time of the incoming pulse
float count; // Calculated Frequency
float freqStart = 90;

void setup() {
  pinMode(capteurPin, INPUT);
  pinMode(actionneurPin, OUTPUT);
  Serial.begin(57600);
  delay(1000);
  Serial.flush();
  Serial.println("début de la com");
  Serial.print("count = ");
  Serial.println(count);
}

void loop() {
    Serial.write("\n");
    pulseHigh = pulseIn(capteurPin, HIGH);
    pulseLow = pulseIn(capteurPin, LOW);
    pulseTotal = pulseHigh + pulseLow; // Time period of the pulse in microseconds
    count = 1000000 / pulseTotal; // Frequency in Hertz (Hz)
    Serial.print("count: ");
    Serial.println(count);
    if (isinf(count)){
      Serial.println("plus de vibrations");
      tone(actionneurPin, freqStart);
      delay(2000);
      noTone(actionneurPin);
      if (freqStart > 119){
        freqStart = 90;
      } else {
        freqStart += 2.5;
      }
    }
    delay(1000);
}
