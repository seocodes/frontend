#AUGUSTO Z. VITALI - 2190
pedido = {}
def add_pedido():
    pratos = []
    nome = input('Nome do cliente: ').lower().capitalize()
    while True:
        prato = input('Prato: ').lower().capitalize()
        pratos.append(prato)
        opcao = input('Deseja pedir outro prato? S/N: ').upper().strip()
        if opcao == 'N':
            break
    pedido[nome] = pratos

def att_pedido():
    for nome, pratos in pedido.items():
        print(f'{nome}: {pratos}')
    nome = input('Nome do cliente para mudar: ').lower().capitalize()
    if nome not in pedido:
        print('Cliente não encontrado')
    else:
        prato_original = input("Qual prato deseja substituir? ").lower().capitalize()
        if prato_original in pedido[nome]:
            indice = pedido[nome].index(prato_original)  #Achar o índice do prato fornecido, pois não dá pra trocar pelo nome eu acho
            prato_novo = input("Qual prato deseja adicionar? ").lower().capitalize()
            pedido[nome][indice] = prato_novo
        else:
            print(f'{prato_original} não foi encontrado na lista de pedidos.')

def del_pedido():
    for nome, pratos in pedido.items():
        print(f'{nome}: {pratos}')
    nome = input('Nome do cliente para mudar: ').lower().capitalize()
    if nome not in pedido:
        print('Cliente não encontrado')
    else:
        prato_remove = input('Qual prato deseja excluir? ').lower().capitalize()
        if  prato_remove in pedido[nome]:
            pedido[nome].remove(prato_remove)
        else:
            print('Prato não encontrado.')
    
def filtrar():
    nome = input('Digite o nome do cliente que quer ter os pratos vistos: ').lower().capitalize()
    if nome in pedido.keys():
        print(f'Pratos pedidos por {nome}: {pedido[nome]}')
    else:
        print('Cliente não encontrado')

def visualizar():
    for nome,pratos in sorted(pedido.items()):
        print(f'{nome}: {pratos}')

def sair():
    exit()

while True:
    print('''MENU DE OPÇÕES:
          1 - Adicionar pedido
          2 - Atualizar pedido
          3 - Remover pedido
          4 - Filtrar pedidos
          5 - Visualizar
          6 - Sair''')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        add_pedido()
    elif op == 2:
        att_pedido()
    elif op == 3:
        del_pedido()
    elif op == 4:
        filtrar()
    elif op == 5:
        visualizar()
    elif op == 6:
        sair()
    else:
        print('Opção inválida. Tente novamente.')
