int RO = 2;
int RI = 3;

int LO = 4;
int LI = 5;

bool L1 = false;
bool L2 = false;
bool R1 = false;
bool R2 = false;


void setup() {
  Serial.begin(9600);
  pinMode(LO, INPUT_PULLUP);
  pinMode(LI, INPUT_PULLUP);
  pinMode(RO, INPUT_PULLUP);
  pinMode(RO, INPUT_PULLUP);

}

void loop() {
  if(digitalRead(4) == LOW){
    Serial.println("LO");

  }
  else if(digitalRead(5) == LOW){
    Serial.println("LI");

  }
  else if(digitalRead(2) == LOW){
    Serial.println("RO");

  }
  else if(digitalRead(3) == LOW){
    Serial.println("RI");

  }

}
