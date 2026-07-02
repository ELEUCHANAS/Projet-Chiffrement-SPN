tab_perm=[3, 0, 4, 6, 7, 1, 2, 5]

def permutation(bloc):
    new_bloc=0
    for i in range(8):
        bit=(bloc >> i) & 1 # Extraction du bit i
        new_bloc |= bit << tab_perm[i] # ajout de bit i dans la position tab_perm[i]
    return new_bloc
def inv_permutation(bloc):
    old_bloc=0
    for i in range(8):
        bit=(bloc >> i) & 1 # Extraction du bit i
        old_bloc |= bit << tab_perm.index(i) # ajout de bit extrait à sa position d’origine
    return old_bloc