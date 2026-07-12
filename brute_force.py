import time
from cipher import chiffrer
 
def brute_force(text,text_chiffre,progressbar,Attack_Percent_label):
    s=time.perf_counter()
    found = False
    progressbar["maximum"] = 65536
    progressbar["value"] = 0
    Attack_Percent_label.config(text="0%")
    progressbar.update_idletasks()
    for i in range(0,65536):
        cle=i
        if (text_chiffre == chiffrer(text,i,0)):
            print("cle :",format(cle,"016b"))
            found = True
            break
        if i % 100 == 0:
            progressbar["value"] = i
            percent = int((i / progressbar["maximum"]) * 100)
            Attack_Percent_label.config(text=f"{percent}%")
            progressbar.update_idletasks()
    progressbar["value"] = progressbar["maximum"]
    Attack_Percent_label.config(text="100%")
    progressbar.update_idletasks()
    f=time.perf_counter()
    if not found:
        return [f-s,"key not found"]
    v16=65536/(f-s)
    v32=2**32 / v16
    v64=2**64 / v16
    print("For 2^16 time :",f-s)
    print("For 2^32 time :",v32)
    print("For 2^64 time :",v64)
    return [f-s,cle]