from utils import RoL

def generer_ss_cle(cle):
    k1 = cle >> 8
    k2 = ((cle << 8) & 0xFFFF) >> 8
    k3 = RoL(cle,3) >> 8
    k4 = RoL(cle,6) >> 8
    k5 = RoL(cle,9) >> 8
    return [k1,k2,k3,k4,k5]