import struct


#int.from_bytes()

x = 1234

print(x.to_bytes(16, 'little'))
print(x.to_bytes(16, 'big'))
print(x.bit_length())