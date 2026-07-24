import base64
from sbox import substitute,inv_substitute
from permutation import permutation,inv_permutation
from key_schedule import generer_ss_cle
from utils import XOR

def chiffrer(msg,cle,cin):
    """
    Chiffre un message donné.
    - msg : texte à chiffrer
    - cle : clé principale (16 bits)
    - cin : type d'entrée (0 = UTF-8, 1 = Hex, 2 = Binaire)
    Retourne le message chiffré dans le format correspondant.
    """
    tab_cle = generer_ss_cle(cle) # génération des sous-clés (key schedule)
    msg_to_encrypt_tab=[]
    encrypted_msg=bytearray()
    match (cin):
        case 0: # Chiffrement UTF-8
            msg_to_encrypt_tab = [c.encode("utf-8")[0] for c in msg]
        case 1: # Chiffrement Hexadécimal
            hex_str = msg.replace(" ", "")
            if len(hex_str) % 2 != 0: # padding
                hex_str += "0"  
            msg_to_encrypt_tab = list(bytes.fromhex(hex_str))
        case 2: # Chiffrement Binaire
            bin_str = str(msg).replace(" ", "")
            if len(bin_str) % 8 != 0: # padding
                bin_str += "0" * (8 - len(bin_str) % 8)
            msg_to_encrypt_tab = [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]
    msg_to_encrypt = ''.join(format(b, '08b') for b in msg_to_encrypt_tab)
    while(len(msg_to_encrypt) >= 8):
        res=int(msg_to_encrypt[:8],2) # extraction d’un bloc de 8 bits
        # Ronde 1-3
        for i in range(3):
            res=XOR(res,tab_cle[i])
            res=substitute(res)
            res=permutation(res)
        # Ronde 4
        res=XOR(res,tab_cle[3])
        res=substitute(res)
        res=XOR(res,tab_cle[4])
        encrypted_msg.append(res)
        msg_to_encrypt=msg_to_encrypt[8:]
    match (cin):
        case 0: # Sortie Hexadécimale
            return encrypted_msg.hex()
        case 1: # Sortie base64
            return base64.b64encode(encrypted_msg).decode("utf-8")
        case 2: # Sortie Binaire
            return ''.join(format(b, '08b') for b in encrypted_msg)

def dechiffrer(msg_crypte,cle,cin):
    """
    Dechiffre un message donné.
    - msg_crypte : texte à Dechiffrer
    - cle : clé principale (16 bits)
    - cin : type d'entrée (0 = Hex, 1 = base64, 2 = Binaire)
    Retourne le message Dechiffré dans le format correspondant.
    """
    tab_cle = generer_ss_cle(cle) # génération des sous-clés (key schedule)
    decrypted_msg=bytearray()
    match (cin):
        case 0: # Déchiffrement Hexadécimal
            hex_str = msg_crypte.replace(" ", "")
            if len(hex_str) % 2 != 0: # padding
                hex_str += "0"  
            bin_str = ''.join(format(b, '08b') for b in bytes.fromhex(hex_str))
        case 1: # Déchiffrement base64
            raw_bytes = base64.b64decode(msg_crypte.encode("utf-8"))
            bin_str = ''.join(format(b, '08b') for b in raw_bytes)
        case 2: # Déchiffrement Binaire
            bin_str = str(msg_crypte).replace(" ", "")
            if len(bin_str) % 8 != 0:
                bin_str += "0" * (8 - len(bin_str) % 8) # padding
    while(len(bin_str) >= 8):
        res=int(bin_str[:8],2) # extraction d’un bloc de 8 bits
        # Ronde 1
        res=XOR(res,tab_cle[4])
        res=inv_substitute(res)
        res=XOR(res,tab_cle[3])
        # Ronde 2-4
        for i in range(2,-1,-1):
            res=inv_permutation(res)
            res=inv_substitute(res)
            res=XOR(res,tab_cle[i])
        decrypted_msg.append(res)
        bin_str=bin_str[8:]
    match (cin):
        case 0: # Sortie UTF-8
            return decrypted_msg.decode("utf-8", errors="replace")
        case 1: # Sortie Hexadécimale
            return decrypted_msg.hex()
        case 2: # Sortie Binaire
            return ''.join(format(b, '08b') for b in decrypted_msg)