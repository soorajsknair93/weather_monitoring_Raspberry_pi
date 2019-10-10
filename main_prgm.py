import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
lcd_rs        = 21  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 20
lcd_d4        = 16
lcd_d5        = 12
lcd_d6        = 7
lcd_d7        = 8
lcd_columns = 16
lcd_rows    = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)
while 1:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.message('Humidity :'+str(int(humidity))+' %')
    
    lcd.set_cursor(0,8)
    lcd.message('Temp :'+str(int(temperature))+' C')

    time.sleep(1)
    