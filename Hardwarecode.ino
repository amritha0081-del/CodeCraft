int relayPin = 7;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(relayPin, HIGH);
    }
    
    if (command == '0') {
      digitalWrite(relayPin, LOW);
    }
  }
}
