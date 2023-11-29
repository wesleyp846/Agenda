AGENDA = {}
def mostrar_contatos():
    print()
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print()
        print('>>>>>>Agenda vazia')
        print()

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['tel'])
        print('E-mail:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print()
    except KeyError:
        print()
        print('>>>>>>Contato inexistente')
        print()
    except Exception as error:
        print()
        print('>>>>>>Um erro inesperado aconteceu')
        print(error)

def ler_detalhes_contato():
        tel = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        endereco = input('Digite o endereço do contato: ')
        return tel, email, endereco

def incluir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel': tel,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print(f'>>>>>>>>Contato {contato} adicionado com sucesso')
    print()
    print('__________________')

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f'>>>>>>>Contato {contato} excluido com sucesso')
        print('__________________')
        print()
    except KeyError:
        print()
        print('>>>>>>Contato inexistente')
        print()
    except Exception as error:
        print()
        print('>>>>>>Um erro inesperado aconteceu')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in  linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, tel, email, endereco)

    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{tel},{email},{endereco}\n')
        print('>>>>>> Agenda exportada com sucesso')
    except:
        print('>>> Algum erro inesperado aconteceu')

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in  linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'tel': tel,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>> database carregado com sucesso')
        print(f'{len(AGENDA)} contatos carregados')
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)



def imprimir_menu():
    print('__________________')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos do CSV')
    print('0 - Fechar agenda')
    print('__________________')

carregar()

while True:
    imprimir_menu()
    opcao = input('Escolha uma opção: ')
    print(opcao)

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print(f'>>>>{contato} já existente')
        except KeyError:
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print(f'>>>>Editando o contato {contato}')
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
        except KeyError:
            print(f'>>>> Contato {contato} inexistente')


    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)

    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)


    elif opcao == '0':
        print()
        print('>>>>Fechado o programa')
        print()
        break

    else:
        print()
        print('>>>>>Opção inválida')
        print()
