import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED():
    def __init__(self,number):
        self.led = number
        GPIO.setup(self.led, GPIO.OUT)
    def lightup(self):
        GPIO.output(self.led, GPIO.HIGH)
    
    def lightoff(self):
        GPIO.output(self.led, GPIO.LOW)
    pass

if __name__ == '__main__':
    led = LED(23)
    led.lightup()
    time.sleep(5)
    led.lightoff()
