def menu():
    print("[1] Inserir contato")
    print("[2] Mostrar todos os contatos")
    print("[3] Buscar contato")
    print("[4] Editar contato")
    print("[5] Ordenar contatos por nome")
    print("[6] Apagar contato")
    print("[0] Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def criarContato(agenda, codigo, nome, telefone):
    contato = {
        "codigo" : codigo,
        "nome" : nome,
        "telefone" : telefone
    }
    return contato

def mostrarContatos(agenda):
    for contato in agenda:
        print(f"{contato["codigo"]} - {contato["nome"]} - {contato["telefone"]}")

def buscarContato(agenda, nome):
    for contato in agenda:
        if nome == contato["nome"]:
            print(f"{contato["codigo"]} - {contato["nome"]} - {contato["telefone"]}")
            break
    else:
        print("Nome não encontrado!!!")

def main():
    agenda = []
    codigo = 0
    while True:
        opcao = menu()
        if opcao == 1:
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.append(criarContato(agenda, codigo, nome, telefone))
            codigo +=1
        elif opcao == 2:
            mostrarContatos(agenda)
        elif opcao == 3:
            nome = input("Nome: ")
            buscarContato(agenda, nome)
        elif opcao == 0:
            break
        else:
            print("Opção inválida!!!")

main()