// https://www.elecrow.com/wiki/index.php?title=Dust_Sensor-_DSM501A
// Connect the Pin_3 of DSM501A to nodeMCU 5V(Vin)
// Connect the Pin_5 of DSM501A to nodeMCU GND
// Connect the Pin_2 of DSM501A to nodeMCU D8
// www.elecrow.com
// http://blog.naver.com/PostView.nhn?blogId=twophase&logNo=220709172472
#include <ESP8266WiFi.h>
#include<string.h>

char  ssid[32];
const char* password = "12345678";
WiFiServer server(80);

int pin = 15;//DSM501A input on NOdeMCU D8
unsigned long duration;
unsigned long starttime;
unsigned long endtime;
unsigned long sampletime_ms = 30000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
float realratio = 0;

#define buf_size 2880
int  buf[buf_size];
unsigned int  buf_idx = 0;
 
void setup()
{
  Serial.begin(115200);
  pinMode(pin,INPUT);

  setupWiFi();
  server.begin();

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
    
  
  for(int i=0; i< buf_size; i++) buf[i]=0;
  starttime = millis(); 
}
void loop()
{
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    duration = pulseIn(pin, LOW);
    lowpulseoccupancy += duration;
    endtime = millis();
    if ((endtime-starttime) > sampletime_ms)
    {
      ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
      realratio = ratio/100;
      concentration = 1.1*pow(realratio,3)-3.8*pow(realratio,2)+520*realratio+0.62; // using spec sheet curve
      buf[buf_idx] = (int)concentration;
      Serial.print(buf[buf_idx]);
      buf_idx++;
      if (buf_idx >= buf_size) buf_idx = 0;
      lowpulseoccupancy = 0;
      Serial.println("");
      starttime = millis();
      }
  } else { 

    // Read the first line of the request
    String req = client.readStringUntil('\r');
    Serial.println(req);
    client.flush();
  
    String s = "HTTP/1.1 200 OK\r\n";
      s += "Content-Type: text/html\r\n\r\n";
      s += "<!DOCTYPE HTML>\r\n<html>\r\n";
      
    if (req.indexOf("/get") == -1) {
        s += "get";
    } else {
       int i;
      s += String(buf_size)+ "," + String(millis())+":";
      for (i = buf_idx; i<buf_size;i++) s += String(buf[i])+",";
      for (i = 0; i<(int)buf_idx; i++) s += String(buf[i])+",";
    } 
    s += "</html>\n";
    client.print(s);
    delay(1);
    Serial.println("Client disonnected");
  }
}

void setupWiFi()
{
  WiFi.mode(WIFI_AP);
  
  // Append the last two bytes of the MAC (HEX'd)
  uint8_t mac[WL_MAC_ADDR_LENGTH];
  WiFi.softAPmacAddress(mac);
  String macID = String(mac[WL_MAC_ADDR_LENGTH - 2], HEX) + String(mac[WL_MAC_ADDR_LENGTH - 1], HEX);
  macID.toUpperCase();
  String AP_NameString = "Dust-" + macID;
  AP_NameString.toCharArray(ssid, AP_NameString.length()+1);
  
  WiFi.softAP(ssid, password);
} 
