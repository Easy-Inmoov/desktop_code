import struct
import serial

class Serializer:
   def __init__(self, device, baudrate=9600, timeout=0.5):
       self.device = serial.Serial(device, baudrate, timeout=timeout)

   def __enter__(self):
        return self

   def send(self, msg):
	print(struct.pack('cccc', msg[0], msg[1], msg[2], msg[3]))
        self.device.write(struct.pack('cccc', msg[0], msg[1], msg[2], msg[3]))

   def receive(self):
        return struct.unpack('cccc',self.device.read(4))

   def __exit__(self, exc_type, exc_value, traceback):
	self.device.close()
