import csv

AGENDA = {}

def carregar_contatos():
    with open('dbagenda.csv') as arquivo:
        leitor = csv.reader(arquivo)
        #next(leitor) # pular cabeçalho
        for linha in leitor:
            nome, tel, email, endereco = linha
            AGENDA[nome] = {
                "tel": tel,
                "email": email,
                "endereco": endereco
            }
    print(f"{len(AGENDA)} contatos carregados!")

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
    exportar_contatos('dbagenda.csv')

def incluir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel': tel,
        'email': email,
        'endereco': endereco,
    }
    print(f'>>>>>>>>Contato dicionado com sucesso')
    salvar()