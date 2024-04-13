import sqlite3

# Conectar ao banco de dados e criá-lo se nao existir

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

# Criar tabela de produtos

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    descricao TEXT,
                    quantidade INTEGER,
                    preco REAL
                )''')

# Criar tabela de vendas

cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY,
                    id_produto INTEGER,
                    quantidade_vendida INTEGER,
                    data_venda TEXT,
                    FOREIGN KEY(id_produto) REFERENCES produtos(id)
                )''')

conexao.commit()

#Funções para gerenciamento de estoque:

# Função para adicionar um produto ao estoque

def adicionar_produto(nome, descricao, quantidade, preco):
    cursor.execute('''INSERT INTO produtos (nome, descricao, quantidade, preco)
                    VALUES (?, ?, ?, ?)''', (nome, descricao, quantidade, preco))
    conexao.commit()
    print("Produto adicionado com sucesso!")

# Função para atualizar informações de um produto no estoque

def atualizar_produto(id_produto, nome, descricao, quantidade, preco):
    cursor.execute('''UPDATE produtos SET nome=?, descricao=?, quantidade=?, preco=?
                    WHERE id=?''', (nome, descricao, quantidade, preco, id_produto))
    conexao.commit()
    print("Informações do produto atualizadas com sucesso!")

# Função para visualizar todos os produtos no estoque

def visualizar_produtos():
    cursor.execute('''SELECT * FROM produtos''')
    produtos = cursor.fetchall()
    print("Produtos em estoque:")
    for produto in produtos:
        print(produto)

# Função para registrar uma venda e atualizar o estoque


def registrar_venda(id_produto, quantidade_vendida, data_venda):
    cursor.execute('''INSERT INTO vendas (id_produto, quantidade_vendida, data_venda)
                    VALUES (?, ?, ?)''', (id_produto, quantidade_vendida, data_venda))
    conexao.commit()
    cursor.execute('''UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?''', (quantidade_vendida, id_produto))
    conexao.commit()
    print("Venda registrada com sucesso!")

# Função para gerar relatórios sobre o estoque

def gerar_relatorio_estoque():
    cursor.execute('''SELECT nome, quantidade FROM produtos''')
    estoque = cursor.fetchall()
    print("Relatório de Estoque:")
    for produto in estoque:
        print(f"{produto[0]}: {produto[1]} unidades")

# Fechar conexão

def fechar_conexao():
    cursor.close()
    conexao.close()

# Exemplo:

adicionar_produto("Camisa", "Camisa branca", 50, 29.99)
adicionar_produto("Calça", "Calça jeans", 30, 49.99)
visualizar_produtos()
registrar_venda(1, 5, "2024-04-15")
gerar_relatorio_estoque()
fechar_conexao()