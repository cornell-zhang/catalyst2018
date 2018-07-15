#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
#include <Process.h>

#define PORT 12

YunServer server(PORT);
YunClient client;

static boolean clientActive = false;

void setup()
{
  // Bridge startup
  Bridge.begin();
  Serial.begin(9600);  // setup the serial terminal
  
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

void loop()
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
        int value = ch - '0';
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


