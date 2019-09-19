#!/usr/bin/python3
my_byte_arr = bytearray(open("overfloat","rb").read())
print(my_byte_arr)
start_offset = 0x00
patch_length = 0x00
patch = bytearray(0x00)   # map(lambda c: chr(x^value), my_byte_arr[start_offset: patch_length])) 
                          #in bytearray if I need to xor a section of the binary with a value
                       
my_byte_arr = my_byte_arr[:start_offset] + patch + my_byte_arr[start_offset + patch_length:]
open("patchedBin","wb").write(my_byte_arr)
