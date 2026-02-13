import json
import os

# Funções para carregar e salvar JSON
def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Cadastro de usuários
def cadastrar_usuario():
    usuarios = carregar_dados("usuarios.json")
    nome = input("Nome: ")
    email = input("Email: ")
    usuario = {"id": len(usuarios)+1, "nome": nome, "email": email}
    usuarios.append(usuario)
    salvar_dados("usuarios.json", usuarios)
    print("Usuário cadastrado!")

# Cadastro de produtos
def cadastrar_produto():
    produtos = carregar_dados("produtos.json")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    produto = {"id": len(produtos)+1, "nome": nome, "preco": preco}
    produtos.append(produto)
    salvar_dados("produtos.json", produtos)
    print("Produto cadastrado!")

# Criar pedido
def criar_pedido():
    usuarios = carregar_dados("usuarios.json")
    produtos = carregar_dados("produtos.json")
    pedidos = carregar_dados("pedidos.json")

    print("\nUsuários cadastrados:")
    for u in usuarios:
        print(u)
    id_usuario = int(input("ID do usuário: "))
    usuario = next((u for u in usuarios if u["id"] == id_usuario), None)
    if not usuario:
        print("Usuário não encontrado!")
        return

    print("\nProdutos disponíveis:")
    for p in produtos:
        print(p)
    ids = input("IDs dos produtos separados por vírgula: ")
    ids_produtos = [int(i.strip()) for i in ids.split(",")]

    itens = []
    total = 0
    for pid in ids_produtos:
        produto = next((p for p in produtos if p["id"] == pid), None)
        if produto:
            itens.append(produto)
            total += produto["preco"]

    pedido = {"id": len(pedidos)+1, "usuario": usuario, "itens": itens, "total": total}
    pedidos.append(pedido)
    salvar_dados("pedidos.json", pedidos)
    print(f"Pedido criado! Total: R${total:.2f}")

# Listar dados
def listar_dados(arquivo):
    dados = carregar_dados(arquivo)
    for item in dados:
        print(item)

# Menu
def menu():
    while True:
        print("\n1 - Cadastrar usuário\n2 - Cadastrar produto\n3 - Criar pedido\n4 - Listar usuários\n5 - Listar produtos\n6 - Listar pedidos\n7 - Sair")
        opcao = input("Escolha: ")
        if opcao=="1": cadastrar_usuario()
        elif opcao=="2": cadastrar_produto()
        elif opcao=="3": criar_pedido()
        elif opcao=="4": listar_dados("usuarios.json")
        elif opcao=="5": listar_dados("produtos.json")
        elif opcao=="6": listar_dados("pedidos.json")
        elif opcao=="7": break
        else: print("Opção inválida!")

if __name__=="__main__":
    menu()
