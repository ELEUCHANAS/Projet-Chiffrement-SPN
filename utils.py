def XOR(b1,b2):
    res=0
    for i in range(8):
        bit1 = (b1 >> i) & 1
        bit2 = (b2 >> i) & 1
        res |= (bit1 ^ bit2) << i
    return res
def RoL(cle,n):
    return (cle << n) & 0xFFFF  | (cle >> 16 - n)