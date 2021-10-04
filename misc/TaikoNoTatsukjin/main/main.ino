int LO = 2;
int LI = 3;

int RO = 4;
int RI = 5;

bool L1 = false;
bool L2 = false;
bool R1 = false;
bool R2 = false;


void setup() {
  Serial.begin(9600);
  pinMode(LO, OUTPUT);
  pinMode(LI, OUTPUT);
  pinMode(RO, OUTPUT);
  pinMode(RO, OUTPUT);

}

void loop() {
  if(digitalRead(LO) == HIGH && L2 == false){
    Serial.println("LO");
    L1 = true;
  }
  else if(digitalRead(LI) == HIGH && L2 == false){
    Serial.println("LI");
    L2 = true;
  }
  else if(digitalRead(RO) == HIGH && L2 == false){
    Serial.println("RO");
    R1 = true;
  }
  else if(digitalRead(RI) == HIGH && L2 == false){
    Serial.println("RI");
    R2 = true;
  }

  if(digitalRead(LO) == LOW){
    L1 = false;
  }
  else if(digitalRead(LI) == LOW){
    L2 = false;
  }
  else if(digitalRead(RO) == LOW){
    R1 = false;
  }
  else if(digitalRead(RI) == LOW){
    R2 = false;
  }
}
