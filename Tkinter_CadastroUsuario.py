import tkinter as tk
import sqlite3

conexao = sqlite3.connect("usuario.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS cadastro1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
)
""")

janela = tk.Tk()
janela.minsize(width=900, height=700)
janela.title("Banana")
def pg3():
    for elemento in janela.winfo_children():
        elemento.destroy()
    def pegar_dados():
        global aviso
        try:
            aviso.place_forget()
        except:
            pass
        e = entrada_emailLogin.get().strip()
        p = entrada_senhaLogin.get().strip()
        funcio.execute("SELECT email,password FROM cadastro1 WHERE email = ? AND password = ?", (e,p))
        resultado = funcio.fetchall()
        if resultado:
            funcio.execute("SELECT username FROM cadastro1 WHERE email = ?", (e,))
            user = funcio.fetchone()
            msg = f"LOGIN FEITO!\nSeja bem vindo {user[0]}!"
        else:
            msg = "SENHA OU EMAIL INCORRETOS!"
        aviso = tk.Label(janela, text= msg, bg="#222626", fg="white", font=("arial", 12, "bold"))
        aviso.place(relx=0.5, rely=0.7, anchor="center")
    tk.Button(janela, text="VOLTAR", command=pg1).place(relx=0.9, rely=0.95, anchor="center", relwidth=0.08,relheight=0.05)
    # Frame2 =======================
    Frame2 = tk.Frame(janela, bd=4, bg="#222626", highlightbackground="darkblue")
    Frame2.place(relx=0.5, rely=0.45,relwidth=0.5, relheight=0.7,anchor="center")
    #=======================
    # email =======================
    emailLogin = tk.Label(Frame2, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.24, rely=0.34, anchor="center")
    entrada_emailLogin = tk.Entry(Frame2, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    entrada_emailLogin.place(relx=0.5,rely=0.4, relwidth=0.6, relheight=0.08,anchor="center")
    #=======================
    # senha =======================
    senhaLogin = tk.Label(Frame2, text="Password", bg ="#222626", fg="white" )
    senhaLogin.place(relx=0.26, rely=0.54, anchor="center")
    entrada_senhaLogin = tk.Entry(Frame2, highlightbackground="black", highlightthickness=2, show="*", font=("Arial", 14))
    entrada_senhaLogin.place(relx=0.5,rely=0.6, relwidth=0.6, relheight=0.08,anchor="center")
    #=======================
    # Titles =======================
    tk.Label(Frame2, text="Login", bg ="#222626", fg="white", font=("Arial", 16, "bold")).place(relx=0.25,rely=0.25,anchor="center")
    tk.Label(Frame2, text="Página de Login", bg="#222626", fg="white",font=("Arial", 16, "bold")).place(relx=0.5,rely=0.1, anchor="center")
    #=======================
    # Send_Button =======================
    tk.Button(Frame2,text="Enviar", bg="#013754", fg="White", command=pegar_dados).place(relx=0.5, rely=0.75,relwidth=0.3,relheight=0.1, anchor="center")
    # =======================
def pg2():
    for elemento in janela.winfo_children():
        elemento.destroy()
    def pegar_all_dados():
        global aviso
        try:
            aviso.place_forget()
        except:
            pass
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
            funcio.execute("SELECT email FROM cadastro1 WHERE email = ?", (e,))
            search = funcio.fetchone()
            if not search is None:
                msg = "EMAIL JÁ CADASTRADO NO SISTEMA!"
        if msg != "":
            aviso = tk.Label(frame_1, text=msg, fg="red", bg="#222626", font=("Arial", 12, "bold"))
        else:
            aviso = tk.Label(frame_1, text="CADASTRO REALIZADO COM SUCESSO!", fg="green", bg="#222626",
                             font=("Arial", 12, "bold"))
            funcio.execute("INSERT INTO cadastro1(username,email,password) VALUES(?,?,?)", (u, e, s))
            conexao.commit()
            print(f"Sucesso: {u}, {e}, {s}")
        aviso.place(relx=0.5, rely=0.93, anchor="center")

    # Frame =======================
    frame_1 = tk.Frame(janela, bd=4, bg="#222626")
    frame_1.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.85, anchor="center")
    # =======================
    tk.Label(frame_1, text="Página de Cadastro", bg="#222626", fg="white", font=("Arial", 18, "bold")).place(relx=0.5, rely=0.05, anchor="center")
    tk.Label(frame_1, text="Create an account", bg="#222626", fg="white", font=("Arial", 14, "bold")).place(relx=0.185, rely=0.15, anchor="w")
    # Username =======================
    nome = tk.Label(frame_1, text="Username", bg="#222626",fg= "white")
    nome.config(font=("Georgia", 10))
    nome.place(relx=0.2, rely=0.26, anchor="w")

    entrada_username = tk.Entry(frame_1, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    entrada_username.place(relx=0.5,rely=0.31, relwidth=0.6, relheight=0.08,anchor="center")
    # =======================

    # Email =======================
    email = tk.Label(frame_1, text="Email", bg="#222626",fg= "white")
    email.config(font=("Georgia", 10))
    email.place(relx=0.2, rely=0.39, anchor="w")
    entrada_email = tk.Entry(frame_1, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    entrada_email.place(relx=0.5,rely=0.44, relwidth=0.6, relheight=0.08,anchor="center")
    # =======================

    # Senha =======================
    Password = tk.Label(frame_1, text="Password", bg="#222626",fg= "white")
    Password.config(font=("Georgia", 10))
    Password.place(relx=0.2, rely=0.52, anchor="w")
    entrada_senha = tk.Entry(frame_1, highlightbackground="black", highlightthickness=2, show="*", font=("Arial", 14))
    entrada_senha.place(relx=0.5,rely=0.57, relwidth=0.6, relheight=0.08,anchor="center")
    # =======================

    # Confirmação Senha =======================
    Password_conf = tk.Label(frame_1, text="Password Confirm", bg="#222626",fg= "white")
    Password_conf.config(font=("Georgia", 10))
    Password_conf.place(relx=0.2, rely=0.65, anchor="w")
    entrada_conf_senha = tk.Entry(frame_1, highlightbackground="black", highlightthickness=2, show="*", font=("Arial", 14))
    entrada_conf_senha.place(relx=0.5,rely=0.7, relwidth=0.6, relheight=0.08,anchor="center")

    # =======================

    enviar = tk.Button(frame_1, text="Enviar",bg="#013754", fg="White", command=pegar_all_dados)
    enviar.place(relx=0.5, rely=0.83, relwidth=0.3, relheight=0.08, anchor="center")

    tk.Button(janela, text="VOLTAR", command=pg1).place(relx=0.9, rely=0.95, anchor="center", relwidth=0.08,relheight=0.05)

def pg1():
    for elemento in janela.winfo_children():
        elemento.destroy()
    janela.config(bg="#121414")
    tk.Label(janela, text="~Sistema de Login radical~",fg="white", bg="#121414", font=("Trebuchet MS", 24, "bold underline")).place(relx=0.5,rely=0.1,anchor="center")
    tk.Button(janela,text="LOGIN", command=pg3).place(relx=0.5,rely=0.40, anchor="center", relwidth=0.2,relheight=0.1)
    tk.Button(janela,text="CADASTRO", command=pg2).place(relx=0.5, rely=0.55, anchor="center", relwidth=0.2,relheight=0.1)
pg1()
janela.mainloop()
conexao.close()
