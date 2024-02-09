from ctypes import c_int, addressof
a = 44
print(addressof(c_int(a)))
