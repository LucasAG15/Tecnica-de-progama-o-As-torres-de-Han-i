import os

# Garante que a pasta exista
os.makedirs("Estrategia_das_torres", exist_ok=True)

tarefas = []

while True:
    try:
        escolha = int(input(
            "AGENDA DE TAREFAS\n"
            "1 - ADICIONAR TAREFA\n"
            "2 - MOSTRAR TAREFAS SALVAS\n"
            "3 - MARCAR TAREFA COMO CONCLUÍDA\n"
            "4 - CRIAR ARQUIVO TXT E SAIR\n> "
        ))
    except ValueError:
        print(" Erro: Digite apenas números de 1 a 4!\n")
        continue

    if escolha == 1:
        tarefa = input("Digite sua tarefa: ")
        tarefas.append(tarefa)
        print(" Tarefa adicionada!\n")

    elif escolha == 2:
        if not tarefas:
            print(" Nenhuma tarefa salva.\n")
        else:
            print("\n Lista de Tarefas:")
            for numero, descricao in enumerate(tarefas, start=1):
                print(f"{numero} - {descricao}")
            print()

    elif escolha == 3:
        if not tarefas:
            print(" Nenhuma tarefa para marcar como concluída.\n")
        else:
            print("\n Tarefas:")
            for numero, descricao in enumerate(tarefas, start=1):
                print(f"{numero} - {descricao}")

            try:
                num = int(input("Escolha o número da tarefa concluída: "))
                if 1 <= num <= len(tarefas):
                    print(f" {tarefas[num-1]} concluída!")
                    tarefas[num-1] += " (✔ concluída)"
                else:
                    print(" Número inválido!")
            except ValueError:
                print("Digite apenas números!\n")

    elif escolha == 4:
        caminho = "PDA/mensagem.txt"
        with open(caminho, "w", encoding="utf-8") as f:
            for descricao in tarefas:
                f.write(descricao + "\n")
        print(f" Arquivo '{caminho}' criado com sucesso!")
        break

    else:
        print(" Opção inválida, tente novamente.\n")

