import time
from cipher import chiffrer
 
def brute_force(text,text_chiffre):
    s=time.perf_counter()
    for i in range(0,65536):
        cle=i
        if (text_chiffre == chiffrer(text,i,0)):
            print("cle :",format(cle,"016b"))
            break
    f=time.perf_counter()
    v16=65536/(f-s)
    v32=2**32 / v16
    v64=2**64 / v16
    print("For 2^16 time :",f-s)
    print("For 2^32 time :",v32)
    print("For 2^64 time :",v64)
brute_force("hello","c5af4a4a36")