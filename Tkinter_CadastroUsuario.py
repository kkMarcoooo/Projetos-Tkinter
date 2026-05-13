import tkinter as tk
import sqlite3

conexao = sqlite3.connect("usuario.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS cadastro(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
)
""")

janela = tk.Tk()
janela.minsize(width=900, height=700)
janela.title("Cadastro Usuário ~")
janela.config(bg="#1f1d19")
def pegar_all_dados():
    global aviso
    try:
        aviso.place_forget()
    except: pass
    u = entrada_username.get().strip()
    e = entrada_email.get().strip()
    s = entrada_senha.get().strip()
    cs = entrada_conf_senha.get().strip()
    msg = ""
    if u == "" or e == "" or s == "" or cs == "":
        msg = "PREENCHA TODOS OS CAMPOS!"
    elif not e.endswith(("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com")):
        msg = "INSIRA EMAIL VÁLIDO!"
    elif s != cs:
        msg = "SENHAS NÂO COINCIDEM"
    elif len(s) < 6:
        msg = "SENHA INVÀLIDA"
    if msg == "":
        funcio.execute("SELECT email FROM cadastro WHERE email = ?", (e,))
        search = funcio.fetchone()
        if not search is None:
            msg = "EMAIL JÁ CADASTRADO NO SISTEMA!"
    if msg!="":
        aviso = tk.Label(janela, text=msg, fg="red", bg="lightblue", font=("Arial", 12, "bold"))
    else:
        aviso = tk.Label(janela, text= "LOGIN FEITO COM SUCESSO!", fg = "green", bg = "lightblue", font=("Arial", 12, "bold"))
        funcio.execute("INSERT INTO cadastro(username,email,password) VALUES(?,?,?)",(u,e,s))
        conexao.commit()
        print(f"Sucesso: {u}, {e}, {s}")
    aviso.place(relx=0.3, rely=0.7, anchor="center")

# Frame =======================
frame_1 = tk.Frame(janela, bd= 4, bg="lightblue", highlightbackground="darkblue", highlightthickness=2)
frame_1.place(relx=0.3,rely=0.45,relwidth=0.5,relheight=0.7,anchor="center")
#=======================


# Username =======================
nome = tk.Label(janela, text="Username: ", bg = "lightblue")
nome.config(font=("Georgia", 10))
nome.place(relx=0.1, rely=0.2, anchor="w")

entrada_username = tk.Entry(janela, highlightbackground="black", highlightthickness=1)
entrada_username.place(relx=0.35, rely=0.2, anchor="center", relwidth=0.2, relheight=0.03)
#=======================

# Email =======================
email = tk.Label(janela, text="Email: ", bg = "lightblue")
email.config(font=("Georgia", 10))
email.place(relx=0.1, rely=0.3, anchor="w")
entrada_email = tk.Entry(janela, highlightbackground="black", highlightthickness=1)
entrada_email.place(relx=0.35, rely=0.3, anchor="center", relwidth=0.2, relheight=0.03)
#=======================

# Senha =======================
Password = tk.Label(janela, text="Password: ", bg = "lightblue")
Password.config(font=("Georgia", 10))
Password.place(relx=0.1, rely=0.4, anchor="w")
entrada_senha = tk.Entry(janela, highlightbackground="black", highlightthickness=1)
entrada_senha.place(relx=0.35, rely=0.4, anchor="center", relwidth=0.2, relheight=0.03)
#=======================

# Confirmação Senha =======================
Password_conf = tk.Label(janela, text="Password Confirm: ", bg = "lightblue")
Password_conf.config(font=("Georgia", 10))
Password_conf.place(relx=0.1, rely=0.5, anchor="w")
entrada_conf_senha = tk.Entry(janela, highlightbackground="black", highlightthickness=1)
entrada_conf_senha.place(relx=0.35, rely=0.5, anchor="center", relwidth=0.2, relheight=0.03)
#=======================

def close_pagina():
    conexao.close()
    janela.destroy()

close = tk.Button(janela,text="Close", command= close_pagina)
close.place(relx=0.8, rely=0.5)
enviar = tk.Button(janela, text="Enviar", command=pegar_all_dados)
enviar.place(relx=0.3, rely=0.6, relwidth=0.2,relheight=0.05, anchor="center")


janela.mainloop()