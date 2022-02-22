int light;

void setup() {
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  light = analogRead(A0);
  Serial.println(light);
  digitalWrite(13, HIGH); 
  delay(100);
  
}
