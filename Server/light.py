import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import RPi.GPIO as GPIO
import time
from adafruit_mcp3xxx.analog_in import AnalogIn


class LightSensor():
    def __init__(self, i, stop):
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
        if self.channel.voltage < 2.2:
            self.taken = 0
            return 0
        else:
            # print(self.channel.voltage )
            self.taken = 1
            return 1

if __name__ == "__main__":
    lg = LightSensor(1, 17)
    while True:
        lg.hasCar()
