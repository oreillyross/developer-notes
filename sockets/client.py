import socket
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4571))
    while True:
        msg = s.recv(1024)
        if not msg:
            print('no message from server, closing')
            break
        print('Type of message', type(msg))
        print(msg)
        unpickle = pickle.loads(msg)
        print(unpickle)
        print(type(unpickle))
