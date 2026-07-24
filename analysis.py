import matplotlib.pyplot as plt
import random
from utils import Comparer
from cipher import chiffrer
def Calcul_Effet_Avalanche():
    """
    Calcule et affiche l'effet avalanche sur plusieurs blocs aléatoires.
    - Génère 3 blocs binaires aléatoires (8 bits chacun)
    - Pour chaque bloc, modifie un bit du plaintext et compare les ciphertexts
    - Trace un histogramme du nombre de bits différents (diffusion)
    Retourne un résumé textuel des moyennes avalanche par bloc
    """
    blocs=[format(random.getrandbits(8), '08b') for _ in range(3)] # génération de 3 blocs aléatoires
    plt.figure(figsize=(10,8))
    res = ""
    for j in range(3): # tester sur 3 blocs
        Y=[]
        for i in range(8):
            C1=chiffrer(blocs[j],0b1100101010010101,2)
            bloc_m=format((int(blocs[j],2) ^ (1 << i)),"08b") # flip du bit i
            C2=chiffrer(bloc_m,0b1100101010010101,2)
            Y.append(Comparer(C1,C2))
        # Affichage graphique
        plt.subplot(3,1,j+1)
        plt.bar(range(8),Y)
        plt.yticks(range(0, 9))
        plt.xlabel("Bit modifié")
        plt.ylabel("Bits différents")
        plt.title(f"Bloc {j}: {blocs[j]}")
        res+=f"bloc {j+1} : moyenne avalanche : "+str(round(sum(Y)*100/64,2))+" %\n" # Résultat textuel
    plt.tight_layout()
    plt.savefig("Avalanche_Effect_Result.png")
    plt.close()
    return res