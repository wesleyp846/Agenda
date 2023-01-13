AGENDA = {}

AGENDA['Wesley'] = {
    'tel': '9541988-1118',
    'email': 'aventureiro@gamil',
    'endereco': 'avenida A',
}

AGENDA['Maria'] = {
    'tel': '965442-4268',
    'email': 'wfpere86@gamil',
    'endereco': 'avenida B',
}

def mostrar_contatos():
    print()
    for contato in AGENDA:
        buscar_contato(contato)

def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['tel'])
    print('E-mail:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print()

def incluir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel': tel,
        'email': email,
        'endereco': endereco,
    }
    print()
    print(f'>>>>>>>>Contato {contato} adicionado com sucesso')
    print()
    print('__________________')

def excluir_contato(contato):
    AGENDA.pop(contato)
    print()
    print(f'>>>>>>>Contato {contato} excluido com sucesso')
    print('__________________')
    print()

def imprimir_menu():
    print('__________________')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')
    print('__________________')

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    print(opcao)

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        tel = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        endereco = input('Digite o endereço do contato: ')
        incluir_editar_contato(contato, tel, email, endereco)
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '0':
        print()
        print('>>>>Fechado o programa')
        print()
        break
    else:
        print()
        print('>>>>>Opção inválida')
        print()