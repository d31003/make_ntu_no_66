import socket
import numpy as np
import cv2
import zlib
import time
import math
import struct

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

# TCP connection setting
TCP_IP = '127.0.0.1'                  
TCP_PORT = 11112
cap = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
cong_flag = b"n"

while(True):   
    ret, frame = cap.read()
    # case for normal net speed 
    if cong_flag == b'n':
        frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
    # case for congestion control
    elif cong_flag == b'c':
        frame = cv2.resize(frame, (160, 120), interpolation=cv2.INTER_AREA)
    cv2.imshow('frame',frame)
    flattened = frame.flatten ()
    message = flattened.tostring ()
    compressed = zlib.compress(message, -1)
    send_msg(sock, compressed)
    cong_flag = recv_msg(sock)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destructor
cap.release()
cv2.destroyAllWindows()