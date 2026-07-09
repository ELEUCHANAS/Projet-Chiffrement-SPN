import matplotlib.pyplot as plt
import random
from utils import Comparer
from cipher import chiffrer,dechiffrer

def Calcul_Effet_Avalanche():
    blocs=[format(random.getrandbits(8), '08b') for _ in range(5)]
    plt.figure(figsize=(10,8))
    for j in range(5):
        Y=[]
        for i in range(8):
            C1=chiffrer(blocs[j],0b1100101010010101,2)
            bloc_m=format((int(blocs[j],2) ^ (1 << i)),"08b")
            C2=chiffrer(bloc_m,0b1100101010010101,2)
            Y.append(Comparer(C1,C2))
        plt.subplot(3,2,j+1)
        plt.bar(range(8),Y)
        plt.yticks(range(0, 9))
        plt.xlabel("Bit modifié")
        plt.ylabel("Bits différents")
        plt.title(f"Bloc {j}: {blocs[j]}")
        print(f"bloc {j+1} : moyenne avalanche :",round(sum(Y)*100/64,2),"%")
    plt.tight_layout()
    plt.show()
Calcul_Effet_Avalanche()