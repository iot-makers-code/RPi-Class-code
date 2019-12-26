// https://www.elecrow.com/wiki/index.php?title=Dust_Sensor-_DSM501A
// Connect the Pin_3 of DSM501A to nodeMCU 5V(Vin)
// Connect the Pin_5 of DSM501A to nodeMCU GND
// Connect the Pin_2 of DSM501A to nodeMCU D8
// www.elecrow.com
// http://blog.naver.com/PostView.nhn?blogId=twophase&logNo=220709172472
#include <ESP8266WiFi.h>
#include<string.h>
#define VERSION  "v1.3.10 2019/11/04"
#define MINI_BUILTIN_LED  2

char  SSID[32];
const char* password = "12345678";
WiFiServer server(80);

int pin = 15;//DSM501A input on NOdeMCU D8
unsigned long duration;
unsigned long starttime;
unsigned long endtime;
unsigned long sampletime_ms = 60000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
float realratio = 0;

#define buf_size 1440
typedef struct _value {
	long ts;
	int  ra;
	int  ds;
} Value;

Value buf[buf_size];
unsigned int  buf_idx = 0;
char str[256];
 
void setup()
{
  Serial.begin(115200);
  delay(10);
  Serial.println(VERSION);
  pinMode(pin,INPUT);
  pinMode(MINI_BUILTIN_LED, OUTPUT);

  setupWiFi();
  server.begin();

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("WiFi SSID : ");
  Serial.print(SSID);
  Serial.print(", AP IP address: ");
  Serial.println(myIP);

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
      realratio = ratio;
      concentration = 1.1*pow(realratio,3)-3.8*pow(realratio,2)+520*realratio+0.62; // using spec sheet curve
      buf[buf_idx].ts = endtime;
      buf[buf_idx].ra = (int)(realratio*100);
      buf[buf_idx].ds = (int)(concentration);
      Serial.print("ratio :");
      Serial.print(ratio);
      Serial.print("/");
      Serial.print(buf[buf_idx].ra);
      Serial.print(", concenturation :");
      Serial.print(buf[buf_idx].ds);
      Serial.println("");
      buf_idx++;
      if (buf_idx >= buf_size) buf_idx = 0;
      lowpulseoccupancy = 0;
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
		"<!DOCTYPE HTML>\r\n<html>\n"
		"<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
		"<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>\n"
		"<title>Air Concenturation</title>\n"
		"<style>.ts{color:gray;} .ra{color:green;} .ds{color:blue;}</style>\n"
		"</head>\n<body>\n"
	  );
	sprintf(str, "<div>Device :<span id='dv'>%s</span>, %s </div>\r\n", SSID, VERSION); 
	client.print(str);
	sprintf(str, "<div>Sensor Time:<span id='ct'>%ld</span>, Count:<span id='cp'>%d</span></div>\r\n", millis(), buf_idx); 
	client.print(str);
	client.print("<div style='width:100%'><canvas id='canvas' width='200' height='208'></canvas></div>\n");

	if (req.indexOf("/data") == -1) {
		client.print("<div id='data' style='display:none;'>\n");
		client.print("<script>var H_RESERVE=.85</script>\n");
	}else {
		client.print("<div id='data'>\n");
		client.print("<script>var H_RESERVE=.25</script>\n");
	}
	client.print(" <div>sensor(센서),time,ratio(*100),concenturtion(농도)</div>\n");
 
	int i;
	char *fmt = (char *)" <div>%s, <span class='ts'>%ld</span>, <span class='ra'>%d</span>, <span class='ds'>%d</span></div>\n";
	for (i=buf_idx-1; i>=0; i--) {
		if (buf[i].ts==0) continue;
		sprintf(str, fmt, SSID, buf[i].ts, buf[i].ra, buf[i].ds); 
		client.print(str);
	}
	//for (i = buf_idx; i<buf_size;i++) {
	for (i=buf_size-1; i>=(int)buf_idx; i--) {
		if (buf[i].ts==0) continue;
		sprintf(str, fmt, SSID, buf[i].ts, buf[i].ra, buf[i].ds); 
		client.print(str);
	}

	client.print(
		"</div>\n"
		"<button type='button' onclick='stf();'>Click to Save</button>\n"
		"<hr><div style='font-size:0.8em;'>(c)2019 <em>anhive</em> All Rights Reserved.</div>\n"
		"<script>\n"
            "var ra = document.getElementsByClassName('ra');\n"
            "var ds = document.getElementsByClassName('ds');\n"
            "var ts = document.getElementsByClassName('ts');\n"
            "function draw() {\n"
            " var canvas = document.getElementById('canvas');\n"
            " if (null==canvas || !canvas.getContext) return;\n"
            " var axes={}, ctx=canvas.getContext('2d');\n"
            " ctx.canvas.width  = window.innerWidth*.95;\n"
            " ctx.canvas.height = window.innerHeight*H_RESERVE;\n"
            " axes.x0 = .5;\n"
            " axes.y0 = .5 + .95*canvas.height;\n"
            " axes.ramax = Math.max.apply(Math,\n"
            "              Array.from(ra).map(function(o) { return o.innerText; }));\n"
            " axes.dsmax = Math.max.apply(Math,\n"
            "              Array.from(ds).map(function(o) { return o.innerText; }));\n"
            " axes.dsmin = Math.min.apply(Math,\n"
            "              Array.from(ds).map(function(o) { return o.innerText; }));\n"
            " axes.average = Array.from(ds).reduce((a, o) => a + parseInt(o.innerText), 0) / ds.length;\n"
            " axes.max = Math.max(axes.ramax,axes.dsmax);\n"
            " axes.scale = 0.9 * canvas.height /  axes.max;\n"
            " axes.unit = (canvas.width * .95) / ds.length;\n"
            " axes.doNegativeX = false;\n"
            " showAxes(ctx,axes);\n"
            " doGraph(ctx,axes,ra,'rgb(11,153,11)',1);\n"
            " doGraph(ctx,axes,ds,'rgb(66,44,255)',2);\n"
            "};\n"
            "\n"
            "function doGraph (ctx,axes,data,color,thick) {\n"
            " var xx, yy, dx=axes.unit, x0=axes.x0, y0=axes.y0, scale=axes.scale;\n"
            " ctx.beginPath();\n"
            " ctx.lineWidth = thick;\n"
            " ctx.strokeStyle = color;\n"
            " for (var i=0;i<data.length;i++) {\n"
            "  xx = dx*i; yy = axes.scale*(data[(data.length-1)-i].innerText);\n"
            "\n"
            "  if (i==0) ctx.moveTo(x0+xx,y0-yy);\n"
            "  else      ctx.lineTo(x0+xx,y0-yy);\n"
            " };\n"
            " ctx.stroke();\n"
            "};\n"
            "\n"
            "function showAxes(ctx,axes) {\n"
            " var x0=axes.x0, w=ctx.canvas.width;\n"
            " var y0=axes.y0, h=ctx.canvas.height; s=axes.scale\n"
            " var xmin = axes.doNegativeX ? 0 : x0;\n"
            " ctx.beginPath();\n"
            " ctx.font = '1em Arial';\n"
            " ctx.strokeStyle = 'rgb(192,192,192)';\n"
            " ctx.strokeText('(0,0)', xmin+5, y0-5);\n"
            " ctx.moveTo(xmin,y0); ctx.lineTo(w,y0);\n"
            " ctx.moveTo(x0,0);    ctx.lineTo(x0,h);\n"
            " ctx.stroke();\n"
            " ctx.beginPath();\n"
            " ctx.strokeStyle = 'rgb(0,0,0)';\n"
            " ctx.strokeText('max: '+axes.dsmax, xmin+12, y0-s*axes.dsmax-10); \n"
            " ctx.strokeText('min: '+axes.dsmin, xmin+12, y0-s*axes.dsmin+10); \n"
            " ctx.strokeStyle = 'rgb(105,105,105)';\n"
            " ctx.moveTo(xmin,y0-s*axes.dsmax); ctx.lineTo(xmin+30,y0-s*axes.dsmax);\n"
            " ctx.moveTo(xmin,y0-s*axes.dsmin); ctx.lineTo(xmin+30,y0-s*axes.dsmin);\n"
            " ctx.stroke();\n"
            " ctx.beginPath();\n"
            " ctx.strokeStyle = 'rgb(0,0,0)';\n"
            " ctx.strokeText('average: '+axes.average, xmin+12, y0-s*axes.average+10); \n"
            " ctx.strokeStyle = 'rgb(0,0,255)';\n"
            " ctx.moveTo(xmin,y0-s*axes.average); ctx.lineTo(w,y0-s*axes.average);\n"
            " ctx.stroke();\n"
            " \n"
            "};\n"
            "draw();\n"
            "\n"
            "stf = function() {\n"
            " var data = document.getElementById('data').innerText.replace(/\\r?\\n/gi,'\\r\\n');;\n"
            " var file = new Blob([data], { type: 'text/plain;charset=utf-8' });\n"
            " var name = 'dust.txt';\n"
            " if (window.navigator.msSaveOrOpenBlob)\n"
            "  window.navigator.msSaveOrOpenBlob(file, name);\n"
            " else {\n"
            "  var a = document.createElement('a');\n"
            "  var url = URL.createObjectURL(file);\n"
            "  a.href = url;\n"
            "  a.download = name;\n"
            "  document.body.appendChild(a);\n"
            "  a.click();\n"
            "  setTimeout(function() {\n"
            "      document.body.removeChild(a);\n"
            "      window.URL.revokeObjectURL(url);\n"
            "  }, 0);\n" 
            " }\n"
            "}\n"
            "\n"
            "Date.prototype.datestr = function() {\n"
            "var mm = this.getMonth() + 1;\n"
            "var dd = this.getDate();\n"
            "var hh = this.getHours();\n"
            "var ii = this.getMinutes();\n"
            "var ss = this.getSeconds();\n"
            "return [(mm>9?'':'0') + mm,(dd>9?'/':'/0')\n"
            "      + dd,(hh>9?' ':' 0') + hh,(ii>9?':':':0')\n"
            "      + ii,(ss>9?':':':0') + ss].join('');\n"
            "};\n"
            "\n"
            "rtime = parseInt(document.getElementById('ct').innerHTML);\n"
            "lt = Date.now();\n"
            "for (e of ts) {\n"
            "  dt =  new Date(lt-rtime+parseInt(e.innerHTML));\n"
            "  e.innerHTML=dt.datestr();\n"
            "}\n"	
            "\n"
            "nextis = function() {\n"	
            " setTimeout(function () {\n"	
            "  location.reload();\n"	
            " }, 60000);\n"	
            "}\n"
            "nextis()\n"
		"</script>\n"
		"</body>\n</html>\n"
    );
    delay(1);
    digitalWrite(MINI_BUILTIN_LED, HIGH);
    Serial.println("Client disonnected");
  }
}

void setupWiFi()
{
  WiFi.mode(WIFI_AP);
  uint8_t mac[WL_MAC_ADDR_LENGTH];
  WiFi.softAPmacAddress(mac);
  sprintf(SSID, "DUST-%02X%02X", mac[WL_MAC_ADDR_LENGTH - 2], mac[WL_MAC_ADDR_LENGTH - 1]);
  WiFi.softAP(SSID, password);
} 
