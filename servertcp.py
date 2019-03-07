import socket
import numpy
import cv2
import zlib
import struct
import time
import detector

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
TCP_IP="192.168.43.94"
#192.168.43.94
TCP_PORT = 11112
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
congest_threshold = 0.18
congest_preflag = b'n'
congest_nextflag = b'c'
detector.initial()

# Start connection
message = b""
sock.listen(0)
client, address = sock.accept()

while True:
    # Measure time between data receive for congestion control
    time_st = time.time()
    data = recv_msg(client)
    time_ed = time.time()
    time_gap = time_ed-time_st
    print(time_gap)

    # Response congestion
    if time_gap > congest_threshold :
        send_msg(client, b'c')
        congest_nextflag = b'c'

    else :
        send_msg(client, b'n')
        congest_nextflag = b'n'
    
    # Processing received data
    try:
        decompressed = zlib.decompress(data, 0, 46080*20)
        frame = numpy.fromstring (decompressed, dtype=numpy.uint8)
        if congest_preflag == b'n':
            frame = frame.reshape(240,320,3)
        elif congest_preflag == b'c':
            frame = frame.reshape(120,160,3)
        else:
            print("congestion error!")
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
        detector.detect(frame)
        cv2.imshow("frame2",frame)
        message = b""
    except zlib.error:
        message = b""
        print("Error! But we don't care XDD")
        pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    congest_preflag = congest_nextflag