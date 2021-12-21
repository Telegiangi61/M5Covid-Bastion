# Xmas Fever control
# ver 1.0
#by gian luigi perrella
from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import wifiCfg
import time
import unit


#initialize string to publish body temp
a = None 
# Using HIVEMQ mqtt broker,  point your browser at http://www.hivemq.com/demos/websocket-client/
# and fill the field ADD NEW TOPIC SUBSCRIPTION with the topic m5s/fever
m5mqtt = M5mqtt('m5Fever', 'broker.mqttdashboard.com', 1883, '', '', 300)

lcd.clear()
setScreenColor(0x111111)
image1 = M5Img(0, 0, "res/xmas_party.jpg", True)
label6 = M5TextBox(30, 10, "XMas Fever control", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
wait_ms(10000)

label6 = M5TextBox(30, 10, "XMas Fever control", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label4 = M5TextBox(60, 60, "", lcd.FONT_DejaVu24,0x00FF00, rotate=0)


#initialize M5Stack NCIR sensor unit
ncir0 = unit.get(unit.NCIR, unit.PORTA)

#initialize wifi connection
wifiCfg.doConnect('your_SSID', 'your_Password')
m5mqtt.start()

temptext = M5TextBox(40, 180, "BODY TEMP:", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
tempval = M5TextBox(210, 180, "0", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label5 = M5TextBox(40, 208, "", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)

while True:
  wait_ms(1000)
  temperatura = (str(ncir0.temperature +4)) # sensor NCIR not so precise, add some value to correct
  a = temperatura
  m5mqtt.publish(str('m5s/fever'),str(a))
  tempval.setText(temperatura)
  label4.setColor(0x00FF00)
  if (str(temperatura) >= '34.50' and str(temperatura) < '37.50'):
            label4.setText("GRANT ACCESS")
            label5.setText("CHECK BODY TEMP OK")
            wait_ms(5000)

  elif str(temperatura) >= '37.60':  #need correction to body temp
    tempval.setColor(0xFF0000)
    label5.setText("CHECK BODY TEMP KO")
    label4.setColor(0xFF0000)
    label4.setText("GRANT DENIED")
    speaker.tone(freq=800, duration=1)
    wait_ms(5000)
    tempval.setColor(0xffffff)
  elif str(temperatura) <= '34.50':
    label5.setText("BODY TEMP TOO LOW")
    label4.setText("")
wait_ms(10000)
