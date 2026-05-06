from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela=Tk()
janela.title=("Cadastro de Paciente")
janela.geometry=("800x400")

abas=ttk.Notebook(janela)
abas.pack(fill="both",expand=True)

aba1=Frame(abas)
abas.add(aba1,text="Pacientes")

aba2=Frame(abas)
abas.add(aba2,text="Pacientes Cadrastrados")

def cadastrar():
    nome=entry_nome.get()
    cpf=entry_cpf.get()
    data_de_nascimento=entry_data_de_nascimento.get()
    telefone=entry_telefone.get()
    email=entry_email.get()
    convenio_sus=entry_convenio_sus.get()
    contato_de_emergencia=entry_contato_de_emergencia.get()
    if nome=="" or cpf=="" or data_de_nascimento=="" or telefone=="" or  email== "" or convenio_sus== "" or contato_de_emergencia== "":
        messagebox.showwarning("Erro","Preencha todos os campos!")
    else:
        tabela.insert("",END,values=(nome,cpf,data_de_nascimento,telefone,email,convenio_sus,contato_de_emergencia))

        entry_nome.delete(0,END)
        entry_cpf.delete(0,END)
        entry_data_de_nascimento.delete(0,END)
        entry_telefone.delete(0,END)
        entry_email.delete(0,END)
        entry_convenio_sus.delete(0,END)
        entry_contato_de_emergencia.delete(0,END)

        messagebox.showinfo("Sucesso","Paciente Cadastrado!")
    
    
Label(aba1,text="Nome Completo").pack(pady=5)
entry_nome= Entry(aba1,width=40)
entry_nome.pack()

Label(aba1,text="CPF").pack(pady=5)
entry_cpf= Entry(aba1,width=40)
entry_cpf.pack()

Label(aba1,text="Data de nascimento").pack(pady=5)
entry_data_de_nascimento=Entry(aba1,width=40)
entry_data_de_nascimento.pack()

Label(aba1,text="Telefone").pack(pady=5)
entry_telefone=Entry(aba1,width=40)
entry_telefone.pack()

Label(aba1,text="Email").pack(pady=5)
entry_email=Entry(aba1,width=40)
entry_email.pack()

Label(aba1,text="Convênio/SUS").pack(pady=5)
entry_convenio_sus=Entry(aba1,width=40)
entry_convenio_sus.pack()

Label(aba1,text="Contato de emergência").pack(pady=5)
entry_contato_de_emergencia=Entry(aba1,width=40)
entry_contato_de_emergencia.pack()

Button(
    aba1,
    text="Cadastrar",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)

colunas=("Nome","CPF","Data de Nascimento","Telefone","Email","Convênio/SUS","Contato de emergência")

tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show="headings")
for col in colunas:
    tabela.heading(col,text=col)
    tabela.column(col,width=150)
tabela.pack(fill="both",expand=True,pady=20)

janela.mainloop()
