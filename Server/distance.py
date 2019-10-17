import RPi.GPIO as GPIO
import time


class DistSensor():
    def __init__(self, i, o):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = i
        self.ECHO = o
        self.pillar = 1
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def detect(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.0001)
        GPIO.output(self.TRIG, False)

        start = time.time()
        end = time.time()

        while GPIO.input(self.ECHO) == False:
            start = time.time()

        while GPIO.input(self.ECHO) == True:
            end = time.time()
        sig_time = end - start
        #GPIO.cleanup()    
        self.distance = sig_time * 34300 / 2 
        return self.distance
    
    def isclose(self):
        if self.detect() < 2.5:
            return 1
        else:
            return 0

if __name__ == "__main__":
    ds1 = DistSensor(16, 18)
    print(ds1.detect())
    GPIO.cleanup()
