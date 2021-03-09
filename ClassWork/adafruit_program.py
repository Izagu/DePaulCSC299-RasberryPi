from Adafruit_CharLCD
import Adafruit_CharLCD
from time import sleep

lcd = Adafruit_CharLCD()
lcd.begin(16,2)

i = 0
while Tue:
    lcd.clear()
        lcd.message('Counting: ' + str(i))
        sleep(1) i = i + 1
