# TOPO DA TORRE(Ferramentas para funcionamento: Import os para manipulação de pastas e arquivos)
import os


# + Comando para criar ou colocar conteudo na pasta "estrategia das torres"
os.makedirs("PDA", exist_ok=True)

tarefas = []  # A BAIXO DO TOPO (Começo do codgo: Delcaraçao de lista)

while True:  # + laço de repetiçao já verdadeiro
    try:  # + comando para melhor tratameto de exeções no codgo, como no exemplo a baixo
        escolha = int(input(  # + variavel declarada com comando "Input" para o usuario escrever o INT na frente siginifica que deve ser obrigatoriamente um inteiro
            "AGENDA DE TAREFAS\n"
            "1 - ADICIONAR TAREFA\n"
            "2 - MOSTRAR TAREFAS SALVAS\n"
            "3 - MARCAR TAREFA COMO CONCLUÍDA\n"
            "4 - CRIAR ARQUIVO TXT E SAIR\n> "
        ))
    except ValueError:  # + Comando caso o usuario não escolha um numero inteiro ou outro numero a cima de 4
        print(" Erro: Digite apenas números de 1 a 4!\n")
        continue  # + Commando para dar continuidade a exeção e evita que o codgo feche
        # CENTRO DA TORRE (Tratamento de dados: Estrutura de escolha )
    if escolha == 1:  # + se a escolha for 1
        # + cria variavel com comando input para para o usuario digitar a tarefa
        tarefa = input("Digite sua tarefa: ")
        # + usa comando append para adicionar a tarefa a lista de tarefas
        tarefas.append(tarefa)
        print(" Tarefa adicionada!\n")

    elif escolha == 2:  # + se a opção for 2
        if not tarefas:  # + se a lista estiver vazia faz o comando a baixo
            print(" Nenhuma tarefa salva.\n")
        else:
            print("\n Lista de Tarefas:")
            # + mostra cada tarefa em ordem de posição e numerada, (para cada numero e descrição numere as descrições da lista de tarefas começando por 1)
            for numero, descricao in enumerate(tarefas, start=1):
                # + função para mostrar para o usuario as tarefas com a permição para inserção de dados de de texto
                print(f"{numero} - {descricao}")
            print()

    elif escolha == 3:      # + se a opção for 3
        if not tarefas:
            print(" Nenhuma tarefa para marcar como concluída.\n")
        else:
            print("\nTarefas:")
            for numero, descricao in enumerate(tarefas, start=1):
                print(f"{numero} - {descricao}")

            try:
                # Comando para o usurio digitar o numero
                num = int(input("Escolha o número da tarefa concluída: "))
                # + verifica se o numero da tarefa estadentro da llista de tarefas
                if 1 <= num <= len(tarefas):
                    # + apos o numero ser escolhido printa a tarefa como concluida
                    print(f" {tarefas[num-1]} concluída!")
                    tarefas[num-1] += " ( concluída)"
                else:
                    print(" Número inválido!")
            except ValueError:
                print(" Digite apenas números!\n")

    elif escolha == 4:  # + se a opção for 4
        caminho = "PDA/mensagem.txt"   #+ localização de onde sera criado o txt
        with open(caminho, "w", encoding="utf-8") as f:  #+ permite a modificação do arquivo txt
            for descricao in tarefas:     #+ para cada descrição que existe na lista de tarefas 
                f.write(descricao + "\n")     #+ toda a lista de tarefas vai preencher o arquivo txt 
        print(f" Arquivo '{caminho}' criado com sucesso!")     #+ comando que mostra para o usuario em qual caminho esta 
        break

    else:
        print(" Opção inválida, tente novamente.\n")




