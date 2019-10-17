import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import RPi.GPIO as GPIO
import time
from publish import Device
from adafruit_mcp3xxx.analog_in import AnalogIn


class LightSensor():
    def __init__(self, i, stop):
        self.device = Device()
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        # Create an MCP3008 object
        mcp = MCP.MCP3008(spi, cs)
        # Create an analog input channel on the MCP3008 pin 0
        self.channel = AnalogIn(mcp, eval("MCP.P" + str(i)))
        self.stop    = stop
        self.taken   = 0

    def detect(self):
        return 'ADC Voltage: ' + str(self.channel.voltage) + 'V'
    
    def hasCar(self):
        self.device.publish('openchirp/device/'+self.device.username + '/light' + str(self.stop), payload=self.channel.voltage, qos=0, retain=True )
        if self.channel.voltage < 2:
            self.taken = 0
            return 0
        else:
            self.taken = 1
            return 1

if __name__ == "__main__":
    lg1 = LightSensor(0, 17)
    lg2 = LightSensor(1, 26)
    lg3 = LightSensor(2, 31)
    lg4 = LightSensor(3, 3)
    while True:
        lg1.hasCar()
        lg2.hasCar()
        lg3.hasCar()
        lg4.hasCar()
