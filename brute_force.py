import time
from cipher import chiffrer
from utils import is_base64,is_binary,is_Hex,is_utf8
def brute_force(text,text_chiffre,progressbar,Attack_Percent_label):
    """
    Lance une attaque par force brute.
    - text : texte clair
    - text_chiffre : texte chiffré
    - progressbar : objet barre de progression pour la GUI
    - Attack_Percent_label : objet label pour la GUI
    Retourne les résultats attendus après l'attaque.
    """
    s=time.perf_counter() # démarrer le chronomètre
    found = False
    progressbar["maximum"] = 65536
    progressbar["value"] = 0
    Attack_Percent_label.config(text="0%") # réinitialiser l’affichage du pourcentage
    progressbar.update_idletasks()
    if is_binary(text) and is_binary(text_chiffre):
        cin=2
    elif is_Hex(text) and is_base64(text_chiffre):
        cin=1
    elif is_utf8(text) and is_Hex(text_chiffre):
        cin=0
    else:
        return -1
    # boucle de brute force
    for i in range(0,65536):
        cle=i
        if (text_chiffre == chiffrer(text,i,cin)): # vérifier si la clé candidate produit le texte chiffré attendu
            found = True
            break
        if i % 100 == 0: # mettre à jour la barre de progression tous les 100 essais
            progressbar["value"] = i
            percent = int((i / progressbar["maximum"]) * 100)
            Attack_Percent_label.config(text=f"{percent}%")
            progressbar.update_idletasks()
    # s’assurer que la barre de progression affiche la complétion
    progressbar["value"] = progressbar["maximum"]
    Attack_Percent_label.config(text="100%")
    progressbar.update_idletasks()
    f=time.perf_counter() # arrêter le chronomètre
    if not found:
        return [f-s,"clé non trouvée"]
    debit=65536/(f-s) # vitesse pour clé 16 bits
    v32=2**32 / debit # vitesse pour clé 32 bits
    v64=2**64 / debit # vitesse pour clé 64 bits
    return [f-s,cle,debit,v32,v64]
