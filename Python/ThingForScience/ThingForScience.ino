void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println(random(30, 40));
  delay(5000);

}
