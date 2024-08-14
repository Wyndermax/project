import json

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo, indent=4)

def adicionar_item(lista):
    descricao = input("Digite a despesa que deseja: ")
    valor = float(input("Agora o valor dela: "))
    lista.append({'descricao': descricao, 'valor': valor})

def mostrar_itens(lista):
    print("Itens adicionados:")
    if not lista:
        print("Nenhum item adicionado.")
    else:
        for i, item in enumerate(lista, start=1):
                  print(f"{i}. {item['descricao']}: R$ {item['valor']:.2f}")

def calcular_soma_total(lista):
    soma_total = sum(item['valor'] for item in lista)
    return soma_total

def excluir_item(lista):
    mostrar_itens(lista)
    if lista:
        try:
            indice = int(input("Digite o número do item que você deseja excluir: "))
            if 1 <= indice <= len(lista):
                excluindo = lista.pop(indice - 1)
                print(f"Item '{excluindo['descricao']}' excluído com sucesso.")
            else:
                print(f"Opção invalida, tente novamente!")
        except ValueError:
            print("Opção errada, por favor insira números!")


def main():
    lista_itens = []

    while True:
                  print("1.Adicione um item")
                  print("2.Mostrar itens")
                  print("3.Mostrar o total")
                  print("4.Excluir item")
                  print("5.Sair")

                  opcao = input("Escolha uma opçao: ")

                  if opcao == '1':
                    adicionar_item(lista_itens)
                  elif opcao == '2':
                    mostrar_itens(lista_itens)
                  elif opcao == '3':
                    soma_total = calcular_soma_total(lista_itens)
                    print(f"Soma total dos valores é de R$ {soma_total:.2f}")
                  elif opcao == '4':
                    excluir_item(lista_itens)
                  elif opcao == '5':
                    print("Saindo..")
                    break
                  else:
                    print("Opção errada, tente novamente!")
if __name__=="__main__":
    main()
