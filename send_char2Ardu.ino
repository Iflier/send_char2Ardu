int delayTime;


void setup() {
  // put your setup code here, to run once:  
  Serial.begin(115200); 
}

void loop() {
  
  String number = "";
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    number += (char)Serial.read();
    delay(10);
    Serial.print(number);
  }
}

