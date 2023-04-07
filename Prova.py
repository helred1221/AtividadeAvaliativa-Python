# código para atividade Avaliativa de Programação de Computadores
def menu_ocorrencias(lista_ocorrencias, id):
    opcao = 1
    while opcao != 0:
        print("\n---Menu de Ocorrências---")
        print("1 - Cadastro de ocorrência")
        print("2 - Listar todas ocorrências")
        print("3 - Listar todas ocorrências ativas")
        print("4 - Buscar Ocorrência por título")
        print("5 - Alterar atividade da ocorrência")
        print("6 - Remover Ocorrência")
        print("7 - Listar por mês")
        print("8 - Listar por palavra")
        print("0 - Sair")
        opcao = int(input("Entre com a opção>>"))
        if opcao == 1:
            print("\n---Cadastro---")
            id += 1
            cadastro(lista_ocorrencias, id)
        elif opcao == 2:
            print("\n---Listagem---")
            listagem(lista_ocorrencias)
        elif opcao == 3:
            print("\nListagem[ATIVAS]")
            listagem_ativas(lista_ocorrencias)
        elif opcao == 4:
            print("\nBusca por título")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("\n***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
            else:
                print("\nOcorrência não encontrada!")
        elif opcao == 5:
            print("\nAlteração de Status de Atividade")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("\n***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja alterar a situação da atividade da ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias[posicao]["status"] = not lista_ocorrencias[posicao]["status"]
                    print("\nAlteração realizada com sucesso!")
                else:
                    print("\nSaindo sem alterações")
            else:
                print("\nOcorrência não encontrada!")
        elif opcao == 6:
            print("\nRemoção de Ocorrência")
            titulo = input("Entre com o título da ocorrência:")
            posicao = buscar_ocorrencia(lista_ocorrencias, titulo)
            if posicao != -1:
                print("\n***Ocorrência Encontrada!***")
                impressao_ocorrencia(lista_ocorrencias[posicao], posicao)
                resp = input("Deseja remover a ocorrência? (sim|não)")
                if resp == "sim":
                    lista_ocorrencias.pop(posicao)
                    print("\nRemoção realizada com sucesso!")
                else:
                    print("\nSaindo sem alterações")
            else:
                print("\nOcorrência não encontrada!")
        elif opcao == 7:
            print("\nListagem por mês")
            mes = input("Digite o mês ao qual está procurando: ")
            listagem_mes(lista_ocorrencias, mes)
        elif opcao == 8:
            print("\n---Listagem por palavra digitada---")
            palavra = input("Entre com a palavra: ")
            listagem_palavra(lista_ocorrencias, palavra)
        elif opcao == 0:
            print("\nSaindo do programa!!!")
        else:
            print("\nOpção Inválida!")


def cadastro(lista_ocorrencias, id):
    titulo = input("Entre com o título da ocorrência:")
    descricao = input("Entre com a descrição da ocorrência:")
    implicacoes = input("Entre com as implicações da ocorrência:")
    em_atividade = input("Está em atividade? (sim|não)")
    status = True if em_atividade == "sim" else False
    prazo = int(input("Entre com a estimativa de prazo em dias:"))
    data_inclusao = input("Entre com a data de inclusão da ocorrência: ")
    ocorrencia = dict(id=id, titulo=titulo, descricao=descricao, implicacoes=implicacoes, status=status, prazo=prazo, data_inclusao=data_inclusao)
    lista_ocorrencias.append(ocorrencia)
    print("Ocorrência cadastrada com sucesso!")


def listagem(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências---")
        for i in range(tamanho):
            impressao_ocorrencia(lista_ocorrencias[i], i)
    else:
        print("\nNão existem ocorrências cadastradas.")


def listagem_ativas(lista_ocorrencias):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de todas as ocorrências ativas---")
        existem_ativas = False
        for i in range(tamanho):
            if lista_ocorrencias[i]["status"] == True:
                impressao_ocorrencia(lista_ocorrencias[i], i)
                existem_ativas = True
        if not existem_ativas:
            print("\nNão existem ocorrências ativas")

    else:
        print("Não existem ocorrências cadastradas.")


def impressao_ocorrencia(ocorrencia, i):
    print("\n### ID ", ocorrencia["id"], "###")
    print("###Ocorrência ", i + 1, "###")
    print("Título:", ocorrencia["titulo"])
    print("Descrição:", ocorrencia["descricao"])
    print("Implicações:", ocorrencia["implicacoes"])
    print("Status:",
          "sim" if ocorrencia["status"] == True
          else "não")
    print("Prazo (em dias):", ocorrencia["prazo"])
    print("Data de Inclusão: ", ocorrencia["data_inclusao"])


def buscar_ocorrencia(lista_ocorrencias, titulo):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        for i in range(tamanho):
            if lista_ocorrencias[i]["titulo"] == titulo:
                return i
        return -1
    else:
        return -1


def listagem_mes(lista_ocorrencias, mes):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("\n---Listagem de ocorrências pelo mês---")
        existe_mes = False
        for i in range(tamanho):
            data_incluida = lista_ocorrencias[i]["data_inclusao"]
            cortado = data_incluida.split("/", 2)
            if cortado[1] == mes:
                impressao_ocorrencia(lista_ocorrencias[i], i)
                existe_mes = True
        if not existe_mes:
            print("\nNão existem ocorrências com o mês digitado!")
    else:
        print("\nNão existem ocorrências cadastradas.")

def listagem_palavra(lista_ocorrencias, palavra):
    tamanho = len(lista_ocorrencias)
    if tamanho > 0:
        print("---Listagem de ocorrências por palavra---")
        existe_palavra = False
        for i in range(tamanho):
            titulo_maiusculo = lista_ocorrencias[i]["titulo"]
            if palavra.upper() in titulo_maiusculo.upper():
                impressao_ocorrencia(lista_ocorrencias[i], i)
                existe_palavra = True
        if not existe_palavra:
            print("Não existem ocorrências com a palavra digitada!")
    else:
        print("\nNão existem ocorrências cadastradas.")


# execução
id = 0
lista_ocorrencias = []
menu_ocorrencias(lista_ocorrencias, id)

