#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
#include <Process.h>

#define PORT #

int state = 0;
int value = -1; 

int pin_motor_left_dir = 12;
int pin_motor_right_dir = 13;
int pin_motor_left_speed = 3;
int pin_motor_right_speed = 11;

int pin_ir = A3;

YunServer server(PORT);
YunClient client;

static boolean clientActive = false;

void setup()
{
  // Bridge startup
  Bridge.begin();
  Serial.begin(9600);  // setup the serial terminal

  //Sets up sensor and motor pins as inputs and outputs
  pinMode(pin_ir, INPUT);
  pinMode(pin_motor_left_dir, OUTPUT);
  pinMode(pin_motor_right_dir, OUTPUT);
  pinMode(pin_motor_left_speed, OUTPUT);
  pinMode(pin_motor_right_speed, OUTPUT);

  digitalWrite(pin_motor_left_dir, LOW);
  digitalWrite(pin_motor_right_dir, LOW);
  analogWrite(pin_motor_left_speed, 0);
  analogWrite( pin_motor_right_speed, 0);
  
  //Sets up WiFi chat server
  server.noListenOnLocalhost();
  server.begin();
  client = server.accept();
  // print ip
  Process p;
  p.runShellCommand("ifconfig");
  while(p.running());
  while (p.available()) {
   char result = p.read();          
   Serial.print(result);         
 } 
 Serial.print("Chat server started, listen to port ");   
 Serial.println(PORT);
}


//Provided receive_value function. Reads predicted number sent by digit rec server and stores it in variable `value`
void receive_value()
{
 //Serial.println("test");
  if (client.connected())
  {
    //if (!clientActive)
      //Serial.println("New client connection.");
      
    clientActive = true;
    
    // Have a connection. Read and echo any input to the serial port
    if (client.available())
    {
      Serial.print("Prediction: ");
      
      while (client.available()) {
        uint8_t ch = client.read();
        value = ch - '0';
        Serial.println(value);
      }
      //Serial.println("\"");
    }
    
    // Send to the client
    //client.println("Hello Client!");
  }
  else // No connection, try to accept one.
  {
    if (clientActive)
    {
      client.stop();
      //Serial.println("Client disconnected.");
    }
      
    clientActive = false;
    
    client = server.accept();
  }
}


void loop()
{
  // put your main code here, to run repeatedly:
}
