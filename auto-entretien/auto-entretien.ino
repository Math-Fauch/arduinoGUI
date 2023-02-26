const int capteurPin = 2;
const int actionneurPin = 3;
int pulseHigh; // Integer variable to capture High time of the incoming pulse
int pulseLow; // Integer variable to capture Low time of the incoming pulse
float pulseTotal; // Float variable to capture Total time of the incoming pulse
float count; // Calculated Frequency
float lastCount;

void setup() {
  pinMode(capteurPin, INPUT);
  pinMode(actionneurPin, OUTPUT);
}

void loop() {
    pulseHigh = pulseIn(capteurPin, HIGH);
    pulseLow = pulseIn(capteurPin, LOW);
    pulseTotal = pulseHigh + pulseLow; // Time period of the pulse in microseconds
    count = 1000000 / pulseTotal; // Frequency in Hertz (Hz)
    while (count == 0 && lastCount != 0){
        // jouer lastCount sur l'actionneur
        tone(actionneurPin, lastCount);
        pulseHigh = pulseIn(capteurPin, HIGH);
        pulseLow = pulseIn(capteurPin, LOW);
        pulseTotal = pulseHigh + pulseLow; // Time period of the pulse in microseconds
        count = 1000000 / pulseTotal; // Frequency in Hertz (Hz)
    }
    lastCount = count;
}
