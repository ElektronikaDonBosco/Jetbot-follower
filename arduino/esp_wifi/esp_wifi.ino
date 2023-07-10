
/* This example is written for Nodemcu Modules */

#include "ESP_Wahaj.h" // importing our library

int green = 16; // pin D0
int blue = 5; // pin D1
int red = 4; // pin D2

String path = "nothing";
void setup(){
  Serial.begin(9600);
  start("MOVISTAR_BC90","Ar2pVbtfKNoVeqncYnjY");  // Wifi details connect to
  // initialize GPIO 5 as an output

  pinMode(green, INPUT);
  pinMode(blue, INPUT);
  pinMode(red, INPUT);
}

void loop(){
  //waitUntilNewReq();  //Waits until a new request from python come

  if(CheckNewReq() == 1)
  {
    if (digitalRead(green)){
      Serial.println("green");
      returnThisStr("green");
    }
    else if (digitalRead(blue)){
      Serial.println("blue");
      returnThisStr("blue");
    }
    else if (digitalRead(red)){
      Serial.println("red");
      returnThisStr("red");
    }
    else {
      Serial.println("none");
      returnThisStr("none");
    }
  }
  
//Serial.println("tesiting....");
//if(pwm == 255) Serial.println("highhhhh");
//if(pwm == 0) Serial.println("lowwwwsssh");
//analogWrite(led,pwm);
  
}