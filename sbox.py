sbox=[0xA,0x3,0xB,0xF,0x6,0x2,0x7,0x4,0x5,0xC,0xD,0xE,0x0,0x1,0x9,0x8]
inv_sbox = [12, 13, 5, 1, 7, 8, 4, 6,15, 14, 0, 2, 9, 10, 11, 3]

def substitute(bloc):
    haut_bloc=(bloc >> 4) # Extraction du nibble haut
    bas_bloc=bloc - (haut_bloc << 4) # Extraction du nibble bas
    return (sbox[haut_bloc] << 4) | sbox[bas_bloc]
def inv_substitute(bloc):
    haut_bloc=(bloc >> 4) # Extraction du nibble haut
    bas_bloc=bloc - (haut_bloc << 4) # Extraction du nibble bas
    return (sbox.index(haut_bloc) << 4) | sbox.index(bas_bloc)