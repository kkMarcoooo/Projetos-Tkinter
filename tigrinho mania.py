import tkinter as tk
import sqlite3
janela = tk.Tk()
janela.title("GRANDE_ONÇÃO")
janela.minsize(width=900, height=700)
conexao = sqlite3.connect("dados_onca.db")
funcio = conexao.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS bancoDeDados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
def menu():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#121212")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212")
    frame_menu.place(relx=0.5,rely=0.1,relwidth=1,relheight=0.2,anchor="center")
    # =====~Title~===========----------
    tk.Label(frame_menu,text="GRANDE ONÇÃO🐆🎲",font=("Palatino Linotype", 24, "bold"), bg="#cc1212",fg="#F5F5F7").place(relx=0.5,rely=0.5,anchor="center")
    #=====~Login~===========----------
    login_button = tk.Button(janela,text="LOGIN",bg="#FFCE00", font=("Georgia", 12),command= login)
    login_button.place(relx=0.5,rely=0.4,relwidth=0.2,relheight=0.075, anchor="center")
    #=====~Register~===========----------
    register_button = tk.Button(janela,text="REGISTER",bg="#12E06A", font=("Georgia", 12), command=cadastro)
    register_button.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.075, anchor="center")
    # =====~Selo~===========----------
    tk.Label(janela, text="⋈ SELO DE HONESTIDADE DA O.N.U ⋈", bg="#121212", fg="#F5F5F7", font=("Arial", 10, "bold")).place(relx=0.02,rely=0.95)

    #~~~~~~EXCLOI~~~~~~~~~~~~~~~~
    tk.Button(janela,text="Pular",command=lets_go_gambling).place(relx=0.1,rely=0.9)


def login():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    def pegar_dados():
        e = email_entry.get().strip()
        p = password_entry.get().strip()
        funcio.execute("SELECT email, password FROM bancoDeDados WHERE email = ? AND password = ?",(e,p))
        busca = funcio.fetchall()
        if not busca:
            msg = "INCORRET EMAIL OR PASSWORD"
            aviso = tk.Label(frame_menu, text=msg, bg="#222626", fg="red", font=("arial", 12, "bold"))
            aviso.place(relx=0.5, rely=0.59, anchor="center")
        else:
            lets_go_gambling()

    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#222626")
    frame_menu.place(relx=0.73,rely=0.5,relwidth=0.5,relheight=0.95,anchor="center")
    # =====~Email~===========----------
    emailLogin = tk.Label(frame_menu, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.14, rely=0.25, anchor="center")
    email_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    email_entry.place(relx=0.5,rely=0.3,relwidth=0.8,relheight=0.08,anchor="center")
    # =====~Password~===========----------
    passwordLogin = tk.Label(frame_menu, text="Password", bg ="#222626", fg="white" )
    passwordLogin.place(relx=0.16, rely=0.45, anchor="center")
    password_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    password_entry.place(relx=0.5,rely=0.5,relwidth=0.8,relheight=0.08,anchor="center")
    # =====~Send~===========----------
    send_button = tk.Button(frame_menu, text="Send", command=pegar_dados)
    send_button.place(relx=0.5,rely=0.68,relwidth=0.5,relheight=0.08, anchor="center")

    tk.Label(janela, text="Login", bg="#222626", fg="White", font=("Agency FB", 28,"bold")).place(relx=0.73, rely=0.08, anchor="center")
    tk.Label(janela, text="🐯", bg="#403f3e", fg="#ffd900", font=("Arial", 90)).place(relx=0.23, rely=0.5,anchor="center")
    tk.Label(janela, text="O N Ç A", bg="#403f3e", fg="#ffd900", font=("Arial", 50)).place(relx=0.23, rely=0.37,anchor="center")
    tk.Button(janela,text="Back", command=menu).place(relx=0.04,rely=0.9)


def cadastro():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")

    def pegar_dados():

        u = username_entry.get()
        e = email_entry.get()
        p = password_entry.get()
        pc = passwordConfirm_entry.get()
        msg = ""
        if u == "" or e == "" or p == "" or pc == "":
            msg = "FILL IN ALL FIELDS"
        elif not e.endswith(("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com")):
            msg = "ENTER A VALID EMAIL"
        elif p != pc:
            msg = "PASSWORDS DO NOT MATCH"
        elif len(p) < 6:
            msg = "ENTER A VALID PASSWORD"
        if msg == "":
            funcio.execute("SELECT email FROM bancoDeDados WHERE email = ?", (e,))
            search = funcio.fetchone()
            if not search is None:
                msg = "EMAIL JÁ CADASTRADO NO SISTEMA!"
        if msg != "":
            aviso = tk.Label(frame_menu, text=msg, fg="red", bg="#222626", font=("Arial", 12, "bold"))
        else:
            aviso = tk.Label(frame_menu, text="CADASTRO REALIZADO COM SUCESSO!", fg="green", bg="#222626",font=("Arial", 12, "bold"))
            funcio.execute("""INSERT INTO bancoDeDados(username, email, password)VALUES (?, ?, ?)""", (u, e, p))
            menu()
            conexao.commit()
        aviso.place(relx=0.5, rely=0.715, anchor="center")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#222626")
    frame_menu.place(relx=0.73,rely=0.5,relwidth=0.5,relheight=0.95,anchor="center")
    # =====~Username~===========----------
    usernameLogin = tk.Label(frame_menu, text="Username", bg ="#222626", fg="white" )
    usernameLogin.place(relx=0.18, rely=0.19, anchor="center")
    username_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    username_entry.place(relx=0.5,rely=0.24,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Email~===========----------
    emailLogin = tk.Label(frame_menu, text="Email", bg ="#222626", fg="white" )
    emailLogin.place(relx=0.16, rely=0.32, anchor="center")
    email_entry = tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14))
    email_entry.place(relx=0.5,rely=0.37,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Password~===========----------
    passwordLogin = tk.Label(frame_menu, text="Password", bg ="#222626", fg="white" )
    passwordLogin.place(relx=0.18, rely=0.45, anchor="center")
    password_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    password_entry.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Password_Confirm~===========----------
    passwordConfirmLogin = tk.Label(frame_menu, text="Password Confirm", bg ="#222626", fg="white" )
    passwordConfirmLogin.place(relx=0.23, rely=0.58, anchor="center")
    passwordConfirm_entry= tk.Entry(frame_menu, highlightbackground="black", highlightthickness=2, font=("Arial", 14), show="*")
    passwordConfirm_entry.place(relx=0.5,rely=0.63,relwidth=0.75,relheight=0.08,anchor="center")
    # =====~Send~===========----------
    send_button = tk.Button(frame_menu, text="Send", command=pegar_dados)
    send_button.place(relx=0.5,rely=0.8,relwidth=0.5,relheight=0.08, anchor="center")
    tk.Label(janela, text="Create Account", bg="#222626", fg="White", font=("Agency FB", 28,"bold")).place(relx=0.73, rely=0.08, anchor="center")
    tk.Label(janela, text="🐯", bg="#403f3e", fg="#ffd900", font=("Arial", 90)).place(relx=0.23, rely=0.5,anchor="center")
    tk.Label(janela, text="O N Ç A", bg="#403f3e", fg="#ffd900", font=("Arial", 50)).place(relx=0.23, rely=0.37,anchor="center")

    tk.Button(janela,text="Back", command=menu).place(relx=0.04,rely=0.9)


def lets_go_gambling():
    for elementos in janela.winfo_children():
        elementos.destroy()
    janela.config(bg="#403f3e")
    # =====~Frame~===========----------
    frame_menu = tk.Frame(janela, bg="#cc1212")
    frame_menu.place(relx=0.5,rely=0.05,relwidth=1,relheight=0.15,anchor="center")
menu()
janela.mainloop()
conexao.close()
