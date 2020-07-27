
#include <MPU6050_tockn.h>
#include <Wire.h>

MPU6050 mpu6050(Wire);

long timer = 0;
float X_out = 0;
float Y_out = 0;
float Z_out = 0;
const int FLEX_PIN1 = A0;
const int FLEX_PIN2 = A1;
const int FLEX_PIN3 = A3;
const int FLEX_PIN4 = A4;
const int FLEX_PIN5 = A5;
const float VCC = 5.00;
float roll,pitch,rollF,pitchF,GyroZ,yaw,previousTime,currentTime,elapsedTime,yawF=0;

void setup() {
  Serial.begin(19200);
  pinMode(FLEX_PIN1, INPUT);
  pinMode(FLEX_PIN2, INPUT);
  pinMode(FLEX_PIN3, INPUT);
  pinMode(FLEX_PIN4, INPUT);
  pinMode(FLEX_PIN5, INPUT);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  
 
}

void loop() {
  mpu6050.update();
  previousTime = currentTime;        // Previous time is stored before the actual time read
  currentTime = millis();            // Current time actual time read
  elapsedTime = (currentTime - previousTime) / 1000; // Divide by 1000 to get seconds


  //flex sensor calculations
  int flex1ADC = analogRead(FLEX_PIN1);
  float flex1V = flex1ADC * VCC / 1023.0;
  
  int flex2ADC = analogRead(FLEX_PIN2);
  float flex2V = flex2ADC * VCC / 1023.0;
  
  int flex3ADC = analogRead(FLEX_PIN3);
  float flex3V = flex3ADC * VCC / 1023.0;

  int flex4ADC = analogRead(FLEX_PIN4);
  float flex4V = flex4ADC * VCC / 1023.0;

  int flex5ADC = analogRead(FLEX_PIN5);
  float flex5V = flex5ADC * VCC / 1023.0;
  
  
  
  
  //mpu calculations
  X_out = mpu6050.getAccX();
  Y_out = mpu6050.getAccY();
  Z_out = mpu6050.getAccZ();
  GyroZ = mpu6050.getGyroZ();
  // Calculate Roll and Pitch (rotation around X-axis, rotation around Y-axis)
  roll = atan(Y_out / sqrt(pow(X_out, 2) + pow(Z_out, 2))) * 180 / PI;
  pitch = atan(-1 * X_out / sqrt(pow(Y_out, 2) + pow(Z_out, 2))) * 180 / PI;
  yaw =  yaw + GyroZ * elapsedTime;
  // Low-pass filter
  rollF = 0.94 * rollF + 0.06 * roll;
  pitchF = 0.94 * pitchF + 0.06 * pitch;
  yawF = 0.94 * yawF + 0.06 * yaw;
  Serial.print(rollF);
  Serial.print("/");
  Serial.print(pitchF);
  Serial.print("/");
  Serial.print(yawF);
  Serial.print("/");
  Serial.print(X_out);
  Serial.print("/");
  Serial.print(Y_out);
  Serial.print("/");
  Serial.print(Z_out);
  Serial.print("/");
  Serial.print(flex1V);
  Serial.print("/");
  Serial.print(flex2V);
  Serial.print("/");
  Serial.print(flex3V);
  Serial.print("/");
  Serial.print(flex4V);
  Serial.print("/");
  Serial.println(flex5V);
  
  
  /*
  if(millis() - timer > 1000){
   
    Serial.println("=======================================================");
    Serial.print("temp : ");Serial.println(mpu6050.getTemp());
    Serial.print("accX : ");Serial.print(mpu6050.getAccX());
    Serial.print("\taccY : ");Serial.print(mpu6050.getAccY());
    Serial.print("\taccZ : ");Serial.println(mpu6050.getAccZ());
  
    Serial.print("gyroX : ");Serial.print(mpu6050.getGyroX());
    Serial.print("\tgyroY : ");Serial.print(mpu6050.getGyroY());
    Serial.print("\tgyroZ : ");Serial.println(mpu6050.getGyroZ());
  
    Serial.print("accAngleX : ");Serial.print(mpu6050.getAccAngleX());
    Serial.print("\taccAngleY : ");Serial.println(mpu6050.getAccAngleY());
  
    Serial.print("gyroAngleX : ");Serial.print(mpu6050.getGyroAngleX());
    Serial.print("\tgyroAngleY : ");Serial.print(mpu6050.getGyroAngleY());
    Serial.print("\tgyroAngleZ : ");Serial.println(mpu6050.getGyroAngleZ());
    
    Serial.print("angleX : ");Serial.print(mpu6050.getAngleX());
    Serial.print("\tangleY : ");Serial.print(mpu6050.getAngleY());
    Serial.print("\tangleZ : ");Serial.println(mpu6050.getAngleZ());
    Serial.println("=======================================================\n");
    
    timer = millis();
    */
  //}

}
