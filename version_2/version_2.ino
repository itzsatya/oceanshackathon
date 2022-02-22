int sensorPin = A1; //define analog pin 2
int value = 0; 
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); 
} 
void loop() {
  value = analogRead(sensorPin); 
  Serial.println(100000-value*100000, DEC);// light intensity
                // high values for bright environment
                // low values for dark environment
  digitalWrite(13, HIGH); 
  delay(100); 
//  value = (value *1023000)/1023;
//  Serial.println(value);
}
