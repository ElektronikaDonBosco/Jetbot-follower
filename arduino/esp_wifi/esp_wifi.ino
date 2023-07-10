
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

int green = 16; // pin D0
int blue = 5; // pin D1
int red = 4; // pin D2

String path = "nothing";
ESP8266WebServer server(80);


//---SETUP---

void setup() {
  Serial.begin(9600);
   WiFi.begin("MOVISTAR_BC90","Ar2pVbtfKNoVeqncYnjY");  // Wifi details connect to
  // initialize GPIO 5 as an output

  pinMode(green, INPUT);
  pinMode(blue, INPUT);
  pinMode(red, INPUT);

  while (WiFi.status() != WL_CONNECTED) {  

    delay(2000);
    Serial.println("Waiting to connect …");
    }

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());                        

  server.on("/temp", handleColor);
   
  server.begin();                                                   
  Serial.println("Server listening");
}


//---LOOP---

void loop() {
  server.handleClient(); 
}

void handleColor() {
  //delay(2000);
  if (digitalRead(green)){
    Serial.println("green");
    path = "green";
  }
  else if (digitalRead(blue)){
    Serial.println("blue");
    path = "/blue";
  }
  else if (digitalRead(red)){
    Serial.println("red");
    path = "red";
  }
  else {
    Serial.println("none");
    path = "/none";
  }
  String message = path;
  server.send(200, "text/plain", message);
}

