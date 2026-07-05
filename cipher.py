from sbox import substitute,inv_substitute
from permutation import permutation,inv_permutation
from key_schedule import generer_ss_cle
from utils import XOR

def chiffrer(msg,cle,cin,cout):
    tab_cle = generer_ss_cle(cle)
    msg_to_encrypt_tab=[]
    encrypted_msg=""
    match (cin):
        case 0: # UTF-8 Encryption
            msg_to_encrypt_tab=[c.encode("utf-8") for c in msg]
        case 1: # Hex Encryption
            pass
        case 2: # Binaire Encryption
            pass
    msg_to_encrypt = ''.join(format(b[0], '08b') for b in msg_to_encrypt_tab)
    while(len(msg_to_encrypt) >= 8):
        res=int(msg_to_encrypt[:8],2)
        for i in range(3):
            res=XOR(res,tab_cle[i])
            res=substitute(res)
            res=permutation(res)
        res=XOR(res,tab_cle[3])
        res=substitute(res)
        res=XOR(res,tab_cle[4])
        encrypted_msg+=format(res, '02x')
        msg_to_encrypt=msg_to_encrypt[8:]
    print(encrypted_msg)

def dechiffrer(msg_crypte,cle):
    tab_cle = generer_ss_cle(cle)
    decrypted_msg=""
    while(len(msg_crypte) >= 8):
        res=int(msg_crypte[:8],2)
        res=XOR(res,tab_cle[4])
        res=inv_substitute(res)
        res=XOR(res,tab_cle[3])
        for i in range(2,-1,-1):
            res=inv_permutation(res)
            res=inv_substitute(res)
            res=XOR(res,tab_cle[i])
        decrypted_msg+=bytes([res]).decode("utf-8", errors="replace")
        msg_crypte=msg_crypte[8:]
    print(decrypted_msg)
chiffrer('hello',0b1100101010010101,0,0)
dechiffrer("1100010110101111010010100100101000110110",0b1100101010010101)