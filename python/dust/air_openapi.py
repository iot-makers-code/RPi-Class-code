
# -*- coding: utf-8 -*- 
"""
   
   drafed by Donghyun Kim. @ 2019.02
   
"""

import xml.etree.ElementTree as elemtree
import urllib.request as request
import urllib.parse as parse
import xml.dom.minidom


API="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?"
TERM="&dataTerm=DAILY"
PAGE="&PageNo=1"
ROW="&numOfRows=1"
KEY="&ServiceKey=SA6y7nRFdqxfnD%2Fkey2W1%2FEiaQH%2FB13qw5dCKWbAG%2Fq%2Fh57%2Ftj7Yo4%2FeqbcGpM%2BmgsBG8RKe%2BfZeOBsTrvzehA%3D%3D"
VER="&ver=1.3"


while True:
   try: 
      #측정소명을 입력받기
      location = input("측정소명 : ")
      location_urlencode = parse.quote(location)
      NAME="&stationName=" + location_urlencode

      # https://www.airkorea.or.kr로 접속 주소 만들그 
      url = API + TERM + PAGE + ROW + KEY + VER + NAME
      print(url)
      print("")

      #URL로 호출한 XML을 읽음
      XML = request.urlopen(url)
      tree = elemtree.ElementTree(file=request.urlopen(url))

      #XML에서 미세먼지(PM10), 초미세먼지(PM2.5) 자료 읽기
      item = tree.find("body").find("items").find("item")
      nowdate  = item.find("dataTime")
      pm10_val = item.find("pm10Value")
      pm25_val = item.find("pm25Value")
      pm10_lev = item.find("pm10Grade1h")
      pm25_lev = item.find("pm25Grade1h")

      #등급을 출력하기 위한 함수
      def lev_switch(lev):
            return {"1" : "좋음" , "2" : "보통" ,
                     "3" : "나쁨" , "4" : "매우나쁨"}.get(lev, "-")

      #결과 출력
      print("측정시간 : " + nowdate.text)
      print("PM-10 농도 : " + pm10_val.text + " ㎍/m³")
      print("PM-10 등급 : " + lev_switch(pm10_lev.text))
      print("PM-2.5 농도 : " + pm25_val.text + " ㎍/m³")
      print("PM-2.5 등급 : " + lev_switch(pm25_lev.text))

   except Exception as e:
      print(str(e))
      pass

