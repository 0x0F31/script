from struct import *
import socket
import telnetlib
import sys


HOST = 'chall.pwnable.tw'
PORT = 10104

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.settimeout(5)

tn = telnetlib.Telnet()
tn.sock = s


def recvuntil(pattern):
  t = ""
  while t.find(pattern) == -1:

    try:
      tmp = s.recv(1)
      tmp = tmp.decode()
    except socket.timeout:
      print("TIMEOUT")
      sys.exit()
    except UnicodeDecodeError:
      tmp = str(tmp)
      continue

    if len(tmp) == 0:
      print("Nothing here")
      break

    t += tmp

  print(t)



def pw(d):
  return pack("<I", d)

def pq(d):
  return pack("<Q", d)
  
def uw(s):
  return unpack("<I" ,s)[0]

def uq(s):
  return unpack("<Q", s)[0]
  
  
  
  
#write below
