sbox=[0xA,0x3,0xB,0xF,0x6,0x2,0x7,0x4,0x5,0xC,0xD,0xE,0x0,0x1,0x9,0x8]
inv_sbox = [12, 13, 5, 1, 7, 8, 4, 6,15, 14, 0, 2, 9, 10, 11, 3]

# Fonction du substitution 
def substitute(bloc):
    """
    Applique une substitution fixe sur 4 bits.
    - bloc : entier (4 bits)
    Retourne le bloc substitué.
    """
    haut_bloc=(bloc >> 4) # Extraction du nibble haut
    bas_bloc=bloc - (haut_bloc << 4) # Extraction du nibble bas
    return (sbox[haut_bloc] << 4) | sbox[bas_bloc]
# Fonction inverse du substitution 
def inv_substitute(bloc):
    """
    Applique la substitution inverse sur 4 bits.
    - bloc : entier (4 bits)
    Retourne le bloc original.
    """
    haut_bloc=(bloc >> 4) # Extraction du nibble haut
    bas_bloc=bloc - (haut_bloc << 4) # Extraction du nibble bas
    return (sbox.index(haut_bloc) << 4) | sbox.index(bas_bloc)