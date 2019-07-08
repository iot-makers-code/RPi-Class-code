// https://www.elecrow.com/wiki/index.php?title=Dust_Sensor-_DSM501A
// Connect the Pin_3 of DSM501A to nodeMCU 5V(Vin)
// Connect the Pin_5 of DSM501A to nodeMCU GND
// Connect the Pin_2 of DSM501A to nodeMCU D8
// www.elecrow.com
// http://blog.naver.com/PostView.nhn?blogId=twophase&logNo=220709172472
#include <ESP8266WiFi.h>
#include<string.h>
#define MINI_BUILTIN_LED  2

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
typedef struct _value {
	long ts;
	int  ds;
} Value;

Value buf[buf_size];
unsigned int  buf_idx = 0;
char str[256];
 
void setup()
{
  Serial.begin(115200);
  pinMode(pin,INPUT);
  pinMode(MINI_BUILTIN_LED, OUTPUT);

  setupWiFi();
  server.begin();

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  Serial.print(", WiFi ssid : ");
  Serial.println(ssid);
    

  memset(buf, 0x00, sizeof(buf));
  //for(int i=0; i< buf_size; i++) buf[i]=0;
  starttime = millis(); 
}
void loop()
{
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    duration = pulseIn(pin, HIGH);
    lowpulseoccupancy += duration;
    endtime = millis();
    if ((endtime-starttime) > sampletime_ms)
    {
      digitalWrite(MINI_BUILTIN_LED, LOW);
      ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
      realratio = ratio/100;
      concentration = 1.1*pow(realratio,3)-3.8*pow(realratio,2)+520*realratio+0.62; // using spec sheet curve
      buf[buf_idx].ts = endtime;
      buf[buf_idx].ds = (int)concentration;
      Serial.print(buf[buf_idx].ds);
      buf_idx++;
      if (buf_idx >= buf_size) buf_idx = 0;
      lowpulseoccupancy = 0;
      Serial.println("");
      delay(1000);
      digitalWrite(MINI_BUILTIN_LED, HIGH);
      starttime = millis();
    } 
  } else { 

    // Read the first line of the request
    String req = client.readStringUntil('\r');
    Serial.println(req);
    client.flush();

	digitalWrite(MINI_BUILTIN_LED, LOW);
    client.print(
		"HTTP/1.1 200 OK\r\n"
		"Content-Type: text/html\r\n\r\n"
		"<!DOCTYPE HTML>\r\n<html>\r\n"
		"<meta name='viewport' content='width=device-width, initial-scale=1.0'>\r\n"
		"<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>\r\n"
		"<title>Air Concenturation</title>\r\n"
		"</head>\r\n<body>\r\n"
	  );
      sprintf(str, "<div>Last Time:<span id='ct'>%ld</span>, Count:<span id='cp'>%d</span></div>\r\n", millis(), buf_idx); 
      client.print(str);
      
    if (req.indexOf("/get") == -1) {
      client.print("get");;
    } else {
      int i;
      //for (i = 0; i<(int)buf_idx; i++) {
      for (i=buf_idx-1; i>=0; i--) {
      	if (buf[i].ts==0) continue;
      	sprintf(str, "<div>%s\t<span class='ts'>%ld</span>\t<span class='ds'>%d</span></div>\r\n", ssid, buf[i].ts, buf[i].ds); 
      	//client.print(String(str))
      	client.print(str);
      }
      //for (i = buf_idx; i<buf_size;i++) {
      for (i=buf_size-1; i>=(int)buf_idx; i--) {
      	if (buf[i].ts==0) continue;
      	sprintf(str, "<div>%s\t<span class='ts'>%ld</span>\t<span class='ds'>%d</span></div>\r\n", ssid, buf[i].ts, buf[i].ds); 
      	//client.print(String(str))
      	client.print(str);
      }
    } 

    client.print(
		"<div style='font-size:0.8em;'>(c)2019 <em>anhive</em> All Rights Reserved.</div>\r\n"
		"<script>\r\n"
		"Date.prototype.yyyymmdd = function() {"
		"var mm = this.getMonth() + 1;"
		"var dd = this.getDate();"
		"var hh = this.getHours();"
		"var ii = this.getMinutes();"
		"var ss = this.getSeconds();"
		"return ["
			"(mm>9 ? '' : '0') + mm,"
			"(dd>9 ? '/' : '/0') + dd,"
			"(hh>9 ? ' ' : ' 0') + hh,"
			"(ii>9 ? ':' : ':0') + ii,"
			"(ss>9 ? ':' : ':0') + ss"
			"].join('');"
		"};\r\n"
		""
		"tss=document.getElementsByClassName('ts');"
		"out = document.getElementById('ct').innerHTML;"
		"lt = Date.now();"
		""
		"for (i=0; i<tss.length; i++) {"
			"e = tss[i];"
			"var dt =  new Date(lt - parseInt(out) + parseInt(e.innerHTML));"
			"e.innerHTML = dt.yyyymmdd();"
		"}"
		"</script>\r\n"
		"</body>\r\n</html>\r\n"
		);
    delay(1);
    digitalWrite(MINI_BUILTIN_LED, HIGH);
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
