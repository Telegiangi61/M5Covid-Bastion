from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x111111)
ncir0 = unit.get(unit.NCIR, unit.PORTA)




label0 = M5TextBox(40, 7, "M5COVID BASTION", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label1 = M5TextBox(21, 74, "BodyTempValue:", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label2 = M5TextBox(200, 76, "0", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label3 = M5TextBox(5, 208, "Test readings Body temp", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)


while True:
  label2.setText(str(ncir0.temperature))
  wait(0.2)
  wait_ms(2)