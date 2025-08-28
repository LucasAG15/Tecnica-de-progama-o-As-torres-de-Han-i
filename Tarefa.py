# TOPO (Dleclara uma variavel que é uma lista vazia que sera aterada ao decorrer do projeto)
tarefas = []

# ANDAR A BAIXO DO TOPO(Estrutura de loop While que sempre é verdadeiro
while True:
    escolha = int(input(                                 # + ESTRUTURA de escollha que interage com o usuario)
        "AGENDA DE TAREFAS\n"
        "1 - ADICIONAR TAREFA\n"
        "2 - MOSTRAR TAREFAS SALVAS\n"
        "3 - MARCAR TAREFA COMO CONCLUÍDA\n"
        "4 - CRIAR ARQUIVO TXT E SAIR\n> "
    ))

    # CENTRO DA TORRE (TRATAMENTO de escolha do usuario com IF, ELIF e ELSE contendo uma tarefa a cada escolha)
    if escolha == 1:
        # +pede pro usuario escrever e adiciona o que foi escrito a variavel lista
        tarefa = input("Digite sua tarefa: ")
        tarefas.append(tarefa)
        print(" Tarefa adicionada!")

    elif escolha == 2:
        print("\n📋 Lista de Tarefas:")  # +lista as tarefas por ordem numerica
        for numero, descricao in enumerate(tarefas, start=1):
            print(f"{numero} - {descricao}")
        print()

    elif escolha == 3:
        print("\n📋 Tarefas:")
        for numero, descricao in enumerate(tarefas, start=1):
            print(f"{numero} - {descricao}")

        # +pede pro usuario escolher um numero e a taréfa com esse numero é marcada como concluida
        num = int(input("Escolha o número da tarefa concluída: "))
        if 1 <= num <= len(tarefas):
            print(f" {tarefas[num-1]} concluída!")
            tarefas[num-1] += " (✔ concluída)"
        else:
            print("Número inválido!")

    # BASE DA TORRE (o Progama se inserra quando o ususario escolhe 4 e com as tarefas criadas e marcadas cria um arquivo TXT, fechando o codgo)
    elif escolha == 4:
        with open("mensagem.txt", "w", encoding="utf-8") as f:
            for descricao in tarefas:
                f.write(descricao + "\n")
        print(" Arquivo 'mensagem.txt' criado com sucesso!")
        break

    else:
        print(" Opção inválida, tente novamente.")
