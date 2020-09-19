from m5stack import *
from m5ui import *
from uiflow import *
import face
import time

setScreenColor(0x111111)



faces_rfid = face.get(face.RFID)
label2 = M5TextBox(32, -3, "M5 COVID BASTION", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label3 = M5TextBox(41, 224, "Test readings RFID", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label0 = M5TextBox(65, 62, "UID:", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label1 = M5TextBox(134, 63, "rfidValue", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)

i = None
n = None
val = None
key = None


def buttonA_wasPressed():
  global i, n, val, key
  faces_rfid.writeBlock(1,'Employee1')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global i, n, val, key
  label1.setText(str(faces_rfid.readBlockStr(1)))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasReleased():
  global i, n, val, key
  i = i - 1
  wait(0.5)
  label0.hide()
  label1.hide()
  n = i % 13
  label2.setText(str(key[int(n - 1)]))
  pass
btnA.wasReleased(buttonA_wasReleased)

def buttonC_wasReleased():
  global i, n, val, key
  i = i + 1
  wait(0.5)
  label0.hide()
  label1.hide()
  n = i % 13
  label2.setText(str(key[int(n - 1)]))
  pass
btnC.wasReleased(buttonC_wasReleased)

def buttonB_wasPressed():
  global i, n, val, key
  label1.hide()
  label2.hide()
  n = i % 13
  label0.setText(str(val[int(n - 1)]))
  pass
btnB.wasPressed(buttonB_wasPressed)


while True:
  if faces_rfid.isCardOn():
    label1.setText(str(faces_rfid.readUid()))
  wait_ms(2)
