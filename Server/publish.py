import paho.mqtt.client as mqtt

class Device(mqtt.Client):
    def __init__(self, username="5da09f0c466cc60c381e0c5b", password='rxXgh220rLcO5BIeAxuGLr84uWEwzjV'):
        super(Device, self).__init__()
        self.host = "mqtt.openchirp.io"
        self.port = 8883
        self.keepalive = 300
        self.username = username
        self.password = password

        # Set access credential
        self.username_pw_set(username, password) #set username and pass
        self.tls_set('cacert.pem')

        # Create a dictionary to save all transducer states
        self.device_state = dict()
                        
        # Connect to the Broker, i.e. OpenChirp
        self.connect(self.host, self.port, self.keepalive)
        self.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            return# print("Connection Successful")
        else:
            print("Connection Unsucessful, rc code = {}".format(rc))
        # Subscribing in on_connect() means that if we lose the connection and reconnect, the subscriptions will be renewed.
                                                                    # Subscribe to all transducers
        self.subscribe("openchirp/device/"+self.username+"/#")
    def on_message(self, client, userdata, msg):
#        print(msg.topic+" "+str(msg.payload.decode()))
                
        # Change Actuator State based on Commands Issued from OpenChirp
        transducer = msg.topic.split("/")[-1]
        self.device_state[transducer] = msg.payload.decode()

    def on_publish(self, client, userdata, result):
        return
# Modify here based on your own device
# Instantiate a client for your device
# smart_light = Device(username, password)
#def main():
#    threshold = 2 # Threshold for turn on/off LED
#    sensor = "light-dependent_resistor"
#    actuator = "light"
                    
    # Initialize
#    smart_light.device_state[sensor] = 0
#    smart_light.device_state[actuator] = 0
                                    
#    while True:
        # Actuate the light based on the command
#        GPIO.output(red_led, int(smart_light.device_state[actuator]))
        # Read from sensor and Publish onto OpenChir
#        sensor_reading = channel.voltage
#        smart_light.publish("openchirp/device/"+username+"/"+sensor, payload=sensor_reading, qos=0, retain=True)
        # Update device stat
#        smart_light.device_state[sensor] = sensor_reading
#        time.sleep(1)
