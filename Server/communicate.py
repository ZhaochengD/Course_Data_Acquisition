import socket
from light import LightSensor
from distance import DistSensor
from LED import LED 

host = ''
port = 5560

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("socket bind complete")
    return s

def setupConnection():
    s.listen(1)
    conn, address = s.accept()
    print("Connect to:" + address[0] + ":" +str(address))
    return conn

def initialSensor():
    ls1 = LightSensor(1, 17)
    ls2 = LightSensor(0, 26)
    ls3 = LightSensor(2, 31)
    ls4 = LightSensor(3, 3)
    return [ls1, ls2, ls3, ls4]

def initialLED():
    led1 = LED(23)
    led2 = LED(4)
    led3 = LED(17)
    led4 = LED(12)
    return {17:led2, 26:led1, 31:led3, 3:led4}

def initialRader():
    rs1 = DistSensor(16, 18)
    return rs1

def formatLightInfo(ls_li, rs1):
    empDict1, empDict2 = {}, {}
    for ls in ls_li:
        empDict1[ls.stop] = ls.hasCar()
    empDict2[rs1.pillar] = rs1.isclose()
    return str(empDict1), str(empDict2)

def dataTransfer(conn):
    # big loop that can send/receive data until told not to
    while True:
        # receive the data
        data = conn.recv(1024)
        data = data.decode('utf-8')
        # split the data such that you separate
        # from the rest of the data
        dataMessage = data.split(' ',1)
        command = dataMessage[0]
        if command == "parking":
            reply = "Welcome to intelligent parking system!"
        elif command == "NEV":
            led_dict = initialLED()
            old_reply, dis_reply = formatLightInfo(initialSensor(), initialRader())
            conn.sendall(str.encode(old_reply))
            while True:
                reply, dis = formatLightInfo(initialSensor(), initialRader())
                if reply:
                    print(str.encode(reply + '\t' + dis))
                    conn.sendall(str.encode(reply + '\t' + dis))
                    sig = conn.recv(4)
                    # print(sig)
                    sig = sig.decode('utf-8')
                    if sig[:2] == 'le' and sig[-2:] != '99':
                        led = led_dict[int(sig[2:])]
                        led.lightup()
                    try:
                        if sig == "stop" or sig[-2:] == '99':
                            led.lightoff()
                            break
                    except:
                        print('our client has left us')
                        continue
                else:
                    continue
        elif command == 'EXIT':
            print('Our client has left us')
            return
        elif command == 'KILL':
            print("our server is shutting down")
            s.close()
            break
        else:
            reply = 'Unknown Command'
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()

s = setupServer()
while True:
    #try:
    conn = setupConnection()
    dataTransfer(conn)

