import tkinter as tk
from tkinter import ttk,messagebox
from cipher import chiffrer,dechiffrer
from utils import is_binary,is_Hex,is_base64
def Init_Encrypt_Frame(win):
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
    Encrypt_Plaintext_Entry = tk.Entry(Encrypt_frame,width=20)
    Encrypt_Key_Entry = tk.Entry(Encrypt_frame,width=20)
    Encrypt_Ciphertext_label = tk.Label(Encrypt_frame,text="")
    Encrypt_title_label.grid(row=0, column=0, columnspan=2, pady=10)
    Encrypt_Plaintext_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Encrypt_Plaintext_Entry.grid(row=1, column=1, padx=5, pady=5)
    Encrypt_Key_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Encrypt_Key_Entry.grid(row=2, column=1, padx=5, pady=5)
    Encrypt_InputType_label.grid(row=3, column=0, padx=5, pady=5)
    Encrypt_box.grid(row=3, column=1, padx=5, pady=5)
    Encrypt_Bouton.grid(row=4, column=0, columnspan=2, pady=10)
    Encrypt_Ciphertext_label.grid(row=5, column=0, columnspan=2, pady=10)
    Encrypt_frame.grid(row=0, column=0, padx=5, pady=5)
def Init_Decrypt_Frame(win):
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
    Decrypt_CipherText_Entry = tk.Entry(Decrypt_frame,width=20)
    Decrypt_Key_Entry = tk.Entry(Decrypt_frame,width=20)
    Decrypt_Plaintext_label = tk.Label(Decrypt_frame,text="",borderwidth=5)
    Decrypt_title_label.grid(row=0, column=0, columnspan=2, pady=10)
    Decrypt_CipherText_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Decrypt_CipherText_Entry.grid(row=1, column=1, padx=5, pady=5)
    Decrypt_Key_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Decrypt_Key_Entry.grid(row=2, column=1, padx=5, pady=5)
    Decrypt_InputType_label.grid(row=3, column=0, padx=5, pady=5)
    Decrypt_box.grid(row=3, column=1, padx=5, pady=5)
    Decrypt_Bouton.grid(row=4, column=0, columnspan=2, pady=10)
    Decrypt_Plaintext_label.grid(row=5, column=0, columnspan=2, pady=10)
    Decrypt_frame.grid(row=0, column=2, padx=5, pady=5)
def Init_sep(win):
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
    Analysis_frame = tk.Frame(win,borderwidth=3)
    Analysis_Title = tk.Label(Analysis_frame,text="Security Analysis")
    Analysis_Avalanche = tk.Button(Analysis_frame,text="Run Avalanche Test")
    Analysis_results_label = tk.Label(Analysis_frame,text="Results :")
    Analysis_results_box = tk.Label(Analysis_frame,text="Res")
    Analysis_Title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    Analysis_Avalanche.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    Analysis_results_label.grid(row=2, column=0, sticky="w", pady=(10, 0))
    Analysis_results_box.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    Analysis_frame.grid(row=2, column=0, padx=50, pady=50)
def Init_Attack_Frame(win):
    Attack_frame = tk.Frame(win,borderwidth=3)
    Attack_title_label = tk.Label(Attack_frame,text="Brute force attack")
    Attack_Plaintext_label = tk.Label(Attack_frame,text="PlainText : ")
    Attack_Plaintext_Entry = tk.Entry(Attack_frame,width=20)
    Attack_CipherText_label = tk.Label(Attack_frame,text="CipherText : ")
    Attack_CipherText_Entry = tk.Entry(Attack_frame,width=20)
    Attack_BruteForceAttack_btn = tk.Button(Attack_frame,text="Start Brute Force Attack")
    Attack_ProgressBar = ttk.Progressbar(Attack_frame,orient="horizontal", length=250, mode="determinate")
    Attack_KeyFound_label = tk.Label(Attack_frame,text="Key Found : ")
    Attack_Exectime_label = tk.Label(Attack_frame,text="Execution Time : ")
    Attack_title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    Attack_Plaintext_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    Attack_Plaintext_Entry.grid(row=1, column=1, padx=5, pady=5)
    Attack_CipherText_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    Attack_CipherText_Entry.grid(row=2, column=1, padx=5, pady=5)
    Attack_BruteForceAttack_btn.grid(row=3, column=0, columnspan=2, pady=10)
    Attack_ProgressBar.grid(row=4, column=0, columnspan=2, pady=5)
    Attack_KeyFound_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=5)
    Attack_Exectime_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=5)
    Attack_frame.grid(row=2, column=2, padx=5, pady=5)
def Gui_Encrypt(event=None):
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
def Init_Gui():
    window = tk.Tk()
    window.title("SPN Cipher")
    window.minsize(510, 510)
    Init_Encrypt_Frame(window)
    Init_sep(window)
    Init_Analysis_Frame(window)
    Init_Decrypt_Frame(window)
    Init_Attack_Frame(window)
    window.mainloop()