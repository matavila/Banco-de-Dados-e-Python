"""
    <------- Integrando Python com SQL ----------->
    A integração entre uma Interface Gráfica do Usuário (GUI), um banco de dados SQLite e a capacidade de exportar dados para o Excel usando Pandas oferece uma solução poderosa para aplicativos de software.
    A GUI proporciona uma interação intuitiva para os usuários, enquanto o SQLite oferece um armazenamento eficiente e local dos dados. Com a biblioteca Pandas, os dados podem ser exportados para o Excel, 
    permitindo aos usuários análises detalhadas em uma planilha.

    Bibliotecas:
        Tkinter: Tkinter é uma biblioteca gráfica padrão em Python para criar interfaces gráficas do usuário (GUI).
        SQLite3: SQLite3 é um módulo em Python que permite interagir com bancos de dados SQLite.
        Pandas: Pandas é uma biblioteca poderosa para manipulação e análise de dados em Python.
    
    Enredo do projeto:
        - Criar o banco de dados e tabela
            . Conexão é a variável responsável pela conexão do banco de dados previamente criado (caso não tenha criado, o mesmo é criado e interligado)
            . Cursor é a variável responsável por fazer a interligação com o banco de dados através da chamada da conexão
            . Através do execute iremos fazer com que o cursor crie uma tabela e que a mesma seja preenchida com as colunas desejadas

        - Criar a interface grafica
            . Através da variável Janela é que iremos chamar a criação da mesma para nossa interface

        - Integrar o banco de dados com o a interface grafica
    
        
    Video-aula -> https://www.youtube.com/watch?v=9z4Uz9Y-TZM&list=WL&index=164&t=1453s
"""
# (1) Primeiro Passo: Exportando as bibliotecas a serem utilizadas
import tkinter as tk
import sqlite3
import pandas as pd
from openpyxl.workbook import Workbook

# (4) Quarto Passo: Criando as funções a serem utilizadas nos botões de ação
def Cadastrar_Clientes():
    Conexao = sqlite3.connect("Clientes.db")      
    Cursor = Conexao.cursor()

    # O uso de : antes do nome da variável serve para mostrar que a mesma é temporária
    # Os valores fornecidos para a função execute sera alimentada a partir de um dicionário
    # com os valores fornecidos pela interface grafica
    Cursor.execute("INSERT INTO Clientes VALUES (:nome, :sobrenome, :email, :telefone)",
        {
            'nome' : Entry_Nome.get(),
            'sobrenome' : Entry_Sobrenome.get(),
            'email' : Entry_Email.get(),
            'telefone' : Entry_Telefone.get(),
        }               
    )  

    Conexao.commit()
    Conexao.close()

    # Limpando as informações inseridas após submenter ao banco de dados
    Entry_Nome.delete(0,"end")
    Entry_Sobrenome.delete(0,"end")
    Entry_Email.delete(0,"end")
    Entry_Telefone.delete(0,"end")
             

def Exportar_Clientes():
    Conexao = sqlite3.connect("Clientes.db")      
    Cursor = Conexao.cursor()

    # Pegando os valores contidos no banco de dados através da função SELECT
    Cursor.execute("SELECT *, oid FROM Clientes")

    # Pegando todos os dados da função select
    Clintes_Cadastrados = Cursor.fetchall()  
    print(Clintes_Cadastrados)
    Clintes_Cadastrados = pd.DataFrame(Clintes_Cadastrados, columns = ['Nome','Sobrenome', 'Email', 'Telefone','ID'])
    Clintes_Cadastrados.to_excel("Bancos_Clientes.xlsx")
    Conexao.commit()
    Conexao.close()

# (2) Segundo Passo: Criando o Banco de Dados utilizando a biblioteca SQlite3
#Conexao = sqlite3.connect("Clientes.db")      
#Cursor = Conexao.cursor()
#Cursor.execute("""
#    CREATE TABLE Clientes (
#               nome text,
#               sobrenome text,
#               email text,
#               telefone text
#    )
#""")
#
#Conexao.commit()
#Conexao.close()

# (3) Terceiro Passo: Criando a interface gráfica utilizando o tkinter
Janela = tk.Tk()

# Definindo o título da Janela
Janela.title("Ferramenta de Cadastro de Clientes")


# Definindo as lables (Texto das caixas)
Label_Nome = tk.Label(Janela,text="Nome:")
Label_Nome.grid(row=0, column=0, pady=10, padx=10)


Label_Sobrenome = tk.Label(Janela,text="Sobrenome:")
Label_Sobrenome.grid(row=1, column=0, pady=10, padx=10)

Label_Email = tk.Label(Janela,text="Email:")
Label_Email.grid(row=2, column=0, pady=10, padx=10)

Label_Telefone = tk.Label(Janela,text="Telefone:")
Label_Telefone.grid(row=3, column=0, pady=10, padx=10)


# Definindo os inputs (Caixa de entrada)
Entry_Nome = tk.Entry(Janela,text="Nome:", width=30)
Entry_Nome.grid(row=0, column=1, pady=10, padx=10)


Entry_Sobrenome = tk.Entry(Janela,text="Sobrenome:", width=30)
Entry_Sobrenome.grid(row=1, column=1, pady=10, padx=10)

Entry_Email = tk.Entry(Janela,text="Email:", width=30)
Entry_Email.grid(row=2, column=1, pady=10, padx=10)

Entry_Telefone = tk.Entry(Janela,text="Telefone:", width=30)
Entry_Telefone.grid(row=3, column=1, pady=10, padx=10)


# Definindo os botões de ação
Botao_Cadastrar = tk.Button(Janela,text="Cadastrar Clientes",command=Cadastrar_Clientes)
Botao_Cadastrar.grid(row=4, column=0, pady=10, padx=10, columnspan=2, ipadx=80)

Botao_Exportar = tk.Button(Janela,text="Exportar Base de Clientes",command= Exportar_Clientes)
Botao_Exportar.grid(row=5, column=0, pady=10, padx=10, columnspan=2, ipadx=80)

Janela.mainloop()


