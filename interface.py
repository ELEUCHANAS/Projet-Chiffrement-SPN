import tkinter as tk
from tkinter import ttk,messagebox
from cipher import chiffrer,dechiffrer
from brute_force import brute_force
from analysis import Calcul_Effet_Avalanche
from utils import is_binary,is_Hex,is_base64

def Init_Encrypt_Frame(win):
    """
    Initialise la frame de chiffrement.
    Contient : champ texte, champ clé, choix du type d'entrée, bouton Encrypt.
    """
    global Encrypt_box
    global Encrypt_Plaintext_Entry
    global Encrypt_Key_Entry
    global Encrypt_Ciphertext_label
    Encrypt_frame = tk.Frame(win,borderwidth=3)
    Encrypt_title_label = tk.Label(Encrypt_frame,text="Encryption")
    Encrypt_Plaintext_label = tk.Label(Encrypt_frame,text="PlainText : ")
    Encrypt_Key_label = tk.Label(Encrypt_frame,text="Key : ")
    Encrypt_InputType_label = tk.Label(Encrypt_frame,text="Input type : ")
    Encrypt_box = ttk.Combobox(Encrypt_frame,values=["UTF-8","Hexadecimal","Binaire"])
    Encrypt_Bouton = tk.Button(Encrypt_frame,text="Encrypt",command=Gui_Encrypt)
    Encrypt_Plaintext_Entry = tk.Entry(Encrypt_frame, width=30)   
    Encrypt_Key_Entry = tk.Entry(Encrypt_frame, width=30)
    Encrypt_Ciphertext_label = tk.Label(Encrypt_frame,text="", wraplength=250)
    Encrypt_title_label.grid(row=0, column=0, columnspan=2, pady=10)
    Encrypt_Plaintext_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Encrypt_Plaintext_Entry.grid(row=1, column=1, padx=5, pady=5)
    Encrypt_Key_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Encrypt_Key_Entry.grid(row=2, column=1, padx=5, pady=5)
    Encrypt_InputType_label.grid(row=3, column=0, padx=5, pady=5)
    Encrypt_box.grid(row=3, column=1, padx=5, pady=5)
    Encrypt_Bouton.grid(row=4, column=0, columnspan=2, pady=10)
    Encrypt_Ciphertext_label.grid(row=5, column=0, columnspan=2, pady=10)
    Encrypt_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
def Init_Decrypt_Frame(win):
    """
    Initialise la frame de dechiffrement.
    Contient : champ texte chiffre, champ clé, choix du type d'entrée, bouton Decrypt.
    """
    global Decrypt_box
    global Decrypt_CipherText_Entry
    global Decrypt_Key_Entry
    global Decrypt_Plaintext_label
    Decrypt_frame = tk.Frame(win,borderwidth=3)
    Decrypt_title_label = tk.Label(Decrypt_frame,text="Decryption")
    Decrypt_CipherText_label = tk.Label(Decrypt_frame,text="CipherText : ")
    Decrypt_Key_label = tk.Label(Decrypt_frame,text="Key : ")
    Decrypt_InputType_label = tk.Label(Decrypt_frame,text="Input type : ")
    Decrypt_box = ttk.Combobox(Decrypt_frame,values=["Hexadecimal","base64","Binaire"])
    Decrypt_Bouton = tk.Button(Decrypt_frame,text="Decrypt",command=Gui_Decrypt)
    Decrypt_CipherText_Entry = tk.Entry(Decrypt_frame, width=30)
    Decrypt_Key_Entry = tk.Entry(Decrypt_frame,width=30)
    Decrypt_Plaintext_label = tk.Label(Decrypt_frame,text="", wraplength=250)
    Decrypt_title_label.grid(row=0, column=0, columnspan=2, pady=10)
    Decrypt_CipherText_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Decrypt_CipherText_Entry.grid(row=1, column=1, padx=5, pady=5)
    Decrypt_Key_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Decrypt_Key_Entry.grid(row=2, column=1, padx=5, pady=5)
    Decrypt_InputType_label.grid(row=3, column=0, padx=5, pady=5)
    Decrypt_box.grid(row=3, column=1, padx=5, pady=5)
    Decrypt_Bouton.grid(row=4, column=0, columnspan=2, pady=10)
    Decrypt_Plaintext_label.grid(row=5, column=0, columnspan=2, pady=10)
    Decrypt_frame.grid(row=0, column=2, padx=15, pady=15, sticky="n")
def Init_sep(win):
    """
    Initialise les séparateurs de la fenêtre principale.
    - Configure la grille (colonnes et lignes avec poids)
    - Ajoute un séparateur vertical entre les colonnes
    - Ajoute un séparateur horizontal entre les lignes
    """
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    separator_v = ttk.Separator(win, orient="vertical")
    separator_v.grid(row=0, column=1, rowspan=3, sticky="ns")
    separator_h = ttk.Separator(win, orient="horizontal")
    separator_h.grid(row=1, column=0,columnspan=3, sticky="ew")
def Init_Analysis_Frame(win):
    """
    Initialise la frame de Analyse.
    Contient : un titre ("Security Analysis"), un bouton pour lancer le test d'avalanche, une zone d'affichage des résultats
    """
    global Analysis_results_box
    Analysis_frame = tk.Frame(win,borderwidth=3)
    Analysis_Title = tk.Label(Analysis_frame,text="Security Analysis")
    Analysis_Avalanche = tk.Button(Analysis_frame,text="Run Avalanche Test",command=Gui_Analysis)
    Analysis_results_label = tk.Label(Analysis_frame,text="Results :")
    Analysis_results_box = tk.Label(Analysis_frame,text="", wraplength=300, justify="left")
    Analysis_Title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    Analysis_Avalanche.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    Analysis_results_label.grid(row=2, column=0, sticky="w", pady=(10, 0))
    Analysis_results_box.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    Analysis_frame.grid(row=2, column=0, padx=15, pady=15, sticky="n")
def Init_Attack_Frame(win):
    """
    Initialise la frame de Analyse.
    Contient : champ texte clair, champ texte chiffré, champ clé, choix du type d'entrée, bouton pour lancer l'attaque, barre de progression avec pourcentage, affichage de la clé trouvée et du temps d'exécution.
    """
    global Attack_Plaintext_Entry
    global Attack_CipherText_Entry
    global Attack_ProgressBar
    global Attack_Exectime_label
    global Attack_KeyFound_label
    global Attack_KeyFound_res
    global Attack_Exectime_res
    global Attack_Percent_label
    global Attack_Debit_label
    global Attack_Debit_res
    global Attack_V32_label
    global Attack_V32_res
    global Attack_V64_label
    global Attack_V64_res
    Attack_frame = tk.Frame(win,borderwidth=3)
    Attack_title_label = tk.Label(Attack_frame,text="Brute force attack")
    Attack_Plaintext_label = tk.Label(Attack_frame,text="PlainText : ")
    Attack_Plaintext_Entry = tk.Entry(Attack_frame,width=30)
    Attack_CipherText_label = tk.Label(Attack_frame,text="CipherText : ")
    Attack_CipherText_Entry = tk.Entry(Attack_frame,width=30)
    Attack_BruteForceAttack_btn = tk.Button(Attack_frame,text="Start Brute Force Attack",command=Gui_Attack)
    Attack_ProgressBar = ttk.Progressbar(Attack_frame, orient="horizontal", length=300, mode="determinate")
    Attack_Percent_label = tk.Label(Attack_frame, text="0%")
    Attack_KeyFound_label = tk.Label(Attack_frame,text="Key Found : ")
    Attack_Exectime_label = tk.Label(Attack_frame,text="Execution Time : ")
    Attack_KeyFound_res = tk.Label(Attack_frame,text="")
    Attack_Exectime_res = tk.Label(Attack_frame,text="")
    Attack_Debit_label = tk.Label(Attack_frame,text="Débit (clés/sec) : ")
    Attack_Debit_res = tk.Label(Attack_frame,text="")
    Attack_V32_label = tk.Label(Attack_frame,text="Temps estimé 32 bits : ")
    Attack_V32_res = tk.Label(Attack_frame,text="")
    Attack_V64_label = tk.Label(Attack_frame,text="Temps estimé 64 bits : ")
    Attack_V64_res = tk.Label(Attack_frame,text="")
    Attack_title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    Attack_Plaintext_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Attack_Plaintext_Entry.grid(row=1, column=1, padx=5, pady=5)
    Attack_CipherText_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Attack_CipherText_Entry.grid(row=2, column=1, padx=5, pady=5)
    Attack_BruteForceAttack_btn.grid(row=3, column=0, columnspan=2, pady=10)
    Attack_Percent_label.grid(row=4, column=2, padx=5, sticky="w")
    Attack_ProgressBar.grid(row=4, column=1, padx=5, pady=5)
    Attack_KeyFound_label.grid(row=5, column=0, sticky="e", pady=5)
    Attack_KeyFound_res.grid(row=5, column=1, sticky="w", pady=5)
    Attack_Exectime_label.grid(row=6, column=0, sticky="e", pady=5)
    Attack_Exectime_res.grid(row=6, column=1, sticky="w", pady=5)
    Attack_Debit_label.grid(row=7, column=0, sticky="e", pady=5)
    Attack_Debit_res.grid(row=7, column=1, sticky="w", pady=5)
    Attack_V32_label.grid(row=8, column=0, sticky="e", pady=5)
    Attack_V32_res.grid(row=8, column=1, sticky="w", pady=5)
    Attack_V64_label.grid(row=9, column=0, sticky="e", pady=5)
    Attack_V64_res.grid(row=9, column=1, sticky="w", pady=5)
    Attack_frame.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")
def Gui_Encrypt(event=None):
    """
    Fonction déclenchée par le bouton Encrypt.
    - Vérifie le type d'entrée choisi
    - Valide la clé (16 bits binaire)
    - Lance le chiffrement et affiche le résultat
    """
    choice = Encrypt_box.get()
    key = Encrypt_Key_Entry.get()
    msg = Encrypt_Plaintext_Entry.get()
    if not choice:
        messagebox.showerror("Erreur","Please select an input type")
        return
    if is_binary(key,16) != True:
        messagebox.showerror("Erreur","Please type a valid 16-bit key")
        return
    match (choice):
        case "UTF-8":
            cin=0
        case "Hexadecimal":
            cin=1
            if is_Hex(msg) != True:
                messagebox.showerror("Erreur","Please type a valid Hexadecimal Plaintext")
                return
        case "Binaire":
            cin=2
            if is_binary(msg) != True:
                messagebox.showerror("Erreur","Please type a valid Binary Plaintext")
                return
    Encrypt_Ciphertext_label.config(text=str(chiffrer(msg,int(key,2),cin)))
def Gui_Decrypt(event=None):
    """
    Fonction déclenchée par le bouton Decrypt.
    - Vérifie le type d'entrée choisi (Hex, base64, Binaire)
    - Valide la clé (16 bits binaire)
    - Lance le déchiffrement et affiche le résultat
    """
    choice = Decrypt_box.get()
    key = Decrypt_Key_Entry.get()
    msg = Decrypt_CipherText_Entry.get()
    if not choice:
        messagebox.showerror("Erreur","Please select an input type")
        return
    if is_binary(key,16) != True:
        messagebox.showerror("Erreur","Please type a valid 16-bit key")
        return
    match (choice):
        case "Hexadecimal":
            cin=0
            if is_Hex(msg) != True:
                messagebox.showerror("Erreur","Please type a valid Hexadecimal Plaintext")
                return
        case "base64":
            cin=1
            if is_base64(msg) != True:
                messagebox.showerror("Erreur","Please type a valid base64 Plaintext")
                return
        case "Binaire":
            cin=2
            if is_binary(msg) != True:
                messagebox.showerror("Erreur","Please type a valid Binary Plaintext")
                return
    Decrypt_Plaintext_label.config(text=str(dechiffrer(msg,int(key,2),cin)))
def Gui_Attack(event=None):
    """
    Fonction déclenchée par le bouton Start Brute Force Attack.
    - Vérifie la présence du texte clair et du texte chiffré
    - Lance l'attaque par force brute
    - Met à jour la barre de progression, le temps d'exécution et la clé trouvée
    """
    plaintext = Attack_Plaintext_Entry.get()
    ciphertext = Attack_CipherText_Entry.get()
    if not plaintext or not ciphertext :
        messagebox.showerror("Erreur","Please provide a plaintext or/and ciphertext")
        return
    res = brute_force(plaintext,ciphertext,Attack_ProgressBar,Attack_Percent_label)
    if res == -1:
        messagebox.showerror("Erreur","Please provide a valide plaintext or ciphertext")
        return
    t = res[0]
    Attack_Exectime_res.config(text=f"{t:.3f} sec")
    if  isinstance(res[1], int):
        Attack_KeyFound_res.config(text=str(format(res[1],"016b")))
        debit = res[2]
        v32 = res[3]
        v64 = res[4]
        Attack_Debit_res.config(text=f"{debit:.2f} clés/sec")
        Attack_V32_res.config(text=f"{v32:.2e} sec")
        Attack_V64_res.config(text=f"{v64:.2e} sec")
    else:
        Attack_KeyFound_res.config(text=res[1])
        Attack_Debit_res.config(text="")
        Attack_V32_res.config(text="")
        Attack_V64_res.config(text="")
def Gui_Analysis(eveny=None):
    """
    Fonction déclenchée par le bouton Run Avalanche Test.
    - Exécute le test d'avalanche
    - Affiche les résultats dans la zone prévue
    """
    Analysis_results_box.config(text=Calcul_Effet_Avalanche())
def Init_Gui():
    """
    Initialise la fenêtre principale de l'application SPN Cipher.
    - Configure la taille et le titre
    - Ajoute les différentes frames (chiffrement, déchiffrement, analyse, attaque brute force)
    - Lance la boucle principale Tkinter
    """
    window = tk.Tk()
    window.title("SPN Cipher")
    window.minsize(900, 700)
    Init_Encrypt_Frame(window)
    Init_sep(window)
    Init_Analysis_Frame(window)
    Init_Decrypt_Frame(window)
    Init_Attack_Frame(window)
    window.mainloop()