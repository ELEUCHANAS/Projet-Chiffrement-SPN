import base64
def XOR(b1,b2):
    res=0
    for i in range(8):
        bit1 = (b1 >> i) & 1
        bit2 = (b2 >> i) & 1
        res |= (bit1 ^ bit2) << i
    return res
def RoL(cle,n):
    return (cle << n) & 0xFFFF  | (cle >> 16 - n)
def Comparer(b1,b2):
    return sum([b1[i] !=b2[i] for i in range(8)])
def is_binary(b,n = None):
    try:
        int(b, 2)
    except Exception:
        return False
    if n is not None and len(b) != n:
        return False
    return True
def is_Hex(h):
    return set(h.upper()).issubset("0 1 2 3 4 5 6 7 8 9 A B C D E F".split(" "))
def is_base64(b):
    try:
        if len(b) % 4 != 0:
            return False
        base64.b64decode(b, validate=True)
        return True
    except Exception:
        return False