# importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# criando janela
jan = Tk()
jan.title("DP systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/logoIcon.ico")


# carregando imagem
logo = PhotoImage(file="icons/logo.png")


# Propriedades da janela
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

# Logo
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

# Username
UserLabel = Label(
    RightFrame,
    text="Username:",
    font=("JetBrains Mono", 20),
    bg="MIDNIGHTBLUE",
    fg="white",
)
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=152, y=112)

# Password
PassLabel = Label(
    RightFrame,
    text="Password:",
    font=("JetBrains Mono", 20),
    bg="MIDNIGHTBLUE",
    fg="white",
)
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=152, y=162)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute(
        """
    SELECT * FROM Users
    WHERE User = ? AND Password = ?
    """,
        (User, Pass),
    )
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if User in VerifyLogin and Pass in VerifyLogin:
            messagebox.showinfo(title="Login Info", message="Acess allowed, welcome!")
    except:
        messagebox.showerror(title="Login Info", message="Acess denied")


# botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=133, y=225)


def Register():
    # removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    # inserindo widgets de cadastro
    NomeLabel = Label(
        RightFrame,
        text="Name:",
        font=("JetBrains Mono", 20),
        bg="MIDNIGHTBLUE",
        fg="white",
    )
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=41)
    NomeEntry.place(x=88, y=18)

    EmailLabel = Label(
        RightFrame,
        text="Email:",
        font=("JetBrains Mono", 20),
        bg="MIDNIGHTBLUE",
        fg="white",
    )
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=38)
    EmailEntry.place(x=104, y=67)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and Email, "" and User == "" and Pass == ""):
            messagebox.showerror(
                title="Register Error", message="Please, fill in all fields"
            )
        else:
            DataBaser.cursor.execute(
                """
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)""",
                (Name, Email, User, Pass),
            )

            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Registered Sucessfully")

    Register = ttk.Button(
        RightFrame, text="Register", width=20, command=RegisterToDataBase
    )
    Register.place(x=133, y=225)

    def BackToLogin():
        # Removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # Voltando widgets de login
        LoginButton.place(x=133, y=225)
        RegisterButton.place(x=133, y=260)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=133, y=260)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=133, y=260)


jan.mainloop()
