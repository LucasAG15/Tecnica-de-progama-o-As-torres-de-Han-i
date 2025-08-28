# TOPO DA TORRE (Dlelaração de variaveis sendo uma lista de numeros e seu limite a baixo )
numeros = []
limite = 6

# ANDAR A BAIXO DO TOPO (Estrutura e interação com o usuario com um laço de repetição que se quebra com uma condição)
while True:
    # + Usuario digita até 5 numeros separados por virgula
    entrada = input("Digite 5 números separados por vírgula: ")

    # CENTRO DA TORRE(Tratamento e modificação de dados)

    # +Separa os numeros cada vaz que o ususario digitar "," virgula
    lista_temp = entrada.split(",")

    # + Garante que os numeros sejam todos inteiros
    lista_temp = [int(n) for n in lista_temp]

    # + Garante que os numeros sejam adicionados a lista um por um, se não a lista adicionaria apenas 1 numero
    numeros.extend(lista_temp)

    # + mostra  o maior numero da lista
    print("O maior número é:", max(numeros))
    # + mostra o menor numero da lista
    print("O menor número é:", min(numeros))

    soma = sum(numeros)         # soma os numeros da lista

    resultado = soma/2          # divide os numeros da lista

    # BASE DA TORRE (O codigo se encerra apos ser mostrado a media dos numeros)
    print("o resultado é", resultado)

    if len(numeros) >= limite:  # + se os numeros forem maiores que o limite o codigo encerra
        break
