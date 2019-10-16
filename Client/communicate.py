import socket
from speaker import Speaker
from network_analysis import Planner
import matplotlib.pyplot as plt
import networkx as nx
import os
import time

host = '172.26.217.178'
port = 5560
im = plt.imread("background.png")
G = nx.read_gpickle("test.gpickle")
Planner = Planner(G, im)
Planner.set_taken([21, 33, 36, 23, 27, 0, 5, 7, 9, 11, 13, 16])
plt.ion()
plt.clf()
plt.axis('off')
plt.text(0.2, 0.5, 'Welcome to intelligent Parking System')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(str.encode("parking"))
reply = s.recv(1024)
print(reply.decode('utf-8'))
os.system('/usr/local/bin/mpg321 welcome.mp3') 

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'KILL':
        s.send(str.encode(command))
        break
    elif command == "NEV":
        s.send(str.encode(command))
        old_reply = eval(s.recv(27))
        print(old_reply)
        for key, val in old_reply.items():
            if val == 1:
                Planner.set_taken(key)
            else:
                Planner.set_empty(key)
        SPOT = Planner.find_nearest()
        if SPOT == 99:
            sig = "stop"
            os.system('/usr/local/bin/mpg321 full.mp3') 
            # break
            plt.clf()
            plt.title('Intelligent Parking System')
            Planner.target()
            plt.pause(1e-17)
            sig = "le" + str(SPOT).zfill(2)
            counter = 1
        else:
            plt.clf()
            plt.title('Intelligent Parking System')
            Planner.target()
            plt.pause(1e-17)
            sig = "le" + str(SPOT).zfill(2)
            Speaker("your nearest parking space is" + str(SPOT))
            counter = 1
        while True:
            Alpha = 0
            recv = s.recv(36)
            print(recv)
            reply, dist = recv.decode('utf-8').split('\t')
            reply = eval(reply)
            dist  = eval(dist)
            s.send(str.encode(sig))
            if sig == "stop" or sig == "le99":
                if sig == 'le99':
                    time.sleep(10)
                plt.close()
                break
            for key, val in reply.items():
                if val == 1:
                    Planner.set_taken(key)
                else:
                    Planner.set_empty(key)
            sig = 'keep'
            if Planner.get_state(SPOT) == 1:
                os.system('/usr/local/bin/mpg321 end.mp3') 
                sig = "stop"
            if list(dist.values())[0] > 0:
                os.system('/usr/local/bin/mpg321 warning.mp3')
                if counter % 2 == 1:
                    Alpha = 1
                else:
                    Alpha = 0.5
            plt.clf()
            plt.title('Intelligent Parking System')
            plt.scatter([77], [277], marker = 'X', color = 'red', alpha=Alpha, s=200)
            Planner.target()
            plt.pause(1e-17)
            counter += 1
        
s.close()
