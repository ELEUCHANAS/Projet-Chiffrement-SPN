import base64
def XOR(b1,b2):
    """
    Effectue un XOR entre deux nombres binaires.
    - b1 : premier nombre binaire (8 bits)
    - b2 : deuxième nombre binaire (8 bits)
    Retourne le résultat du XOR.
    """
    res=0
    for i in range(8): # parcourir bit par bit chaque nombre
        bit1 = (b1 >> i) & 1 # extraire le bit i de b1
        bit2 = (b2 >> i) & 1 # extraire le bit i de b2
        res |= (bit1 ^ bit2) << i # effectuer le XOR sur les bits
    return res
def RoL(cle,n):
    """
    Effectue une rotation circulaire gauche sur 16 bits.
    - cle : valeur entière (16 bits)
    - n : nombre de positions de rotation
    Retourne la valeur obtenue après rotation.
    """
    return (cle << n) & 0xFFFF  | (cle >> (16 - n))
def Comparer(b1,b2):
    """
    compare deux nombres binaires.
    - b1 : premier nombre binaire (8 bits)
    - b2 : deuxième nombre binaire (8 bits)
    Retourne le résultat de la comparaison.
    """
    return sum([b1[i] !=b2[i] for i in range(8)])
def is_binary(b,n = None):
    """
    Teste si une chaîne représente un nombre en base binaire.
    - b : nombre binaire sous forme de chaîne
    - n : taille attendue du nombre binaire (optionnel)
    Retourne True si le test est réussi, False sinon.
    """
    try:
        int(b, 2) # transforme la chaîne binaire en entier
    except Exception:
        return False
    if n is not None and len(b) != n: # verifie la taille si elle est fournie
        return False
    return True
def is_Hex(h):
    """
    Teste si une chaîne représente un nombre en base hexadécimale.
    - h : nombre hexadécimale sous forme de chaîne
    Retourne True si le test est réussi, False sinon.
    """
    return set(h.upper()).issubset("0 1 2 3 4 5 6 7 8 9 A B C D E F".split(" "))
def is_base64(b):
    """
    Teste si une chaîne représente un nombre en base 64.
    - b : nombre base64 sous forme de chaîne
    Retourne True si le test est réussi, False sinon.
    """
    try:
        if len(b) % 4 != 0: # vérifie la propriété du base64 (longueur multiple de 4)
            return False
        base64.b64decode(b, validate=True) # décode  la chaîne base64 en bytes
        return True
    except Exception:
        return False
def is_utf8(text):
    """
    Vérifie si une chaîne est encodable/décodable en UTF-8.
    Retourne True si oui, False sinon.
    """
    try:
        text.encode("utf-8").decode("utf-8")
        return True
    except UnicodeError:
        return False