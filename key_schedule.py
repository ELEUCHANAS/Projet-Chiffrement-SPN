from utils import RoL

def generer_ss_cle(cle):
    """
    Génère les sous-clés (key schedule).
    - cle : clé principale (16 bits)
    Retourne les 5 sous-clés générées.
    """
    k1 = cle >> 8 # bits[0:8] de la clé principale
    k2 = ((cle << 8) & 0xFFFF) >> 8 # bits[8:16] de la clé principale
    k3 = RoL(cle,3) >> 8 # RoL(clé, 3)[0:8]
    k4 = RoL(cle,6) >> 8 # RoL(clé, 6)[0:8]
    k5 = RoL(cle,9) >> 8 # RoL(clé, 9)[0:8]
    return [k1,k2,k3,k4,k5]