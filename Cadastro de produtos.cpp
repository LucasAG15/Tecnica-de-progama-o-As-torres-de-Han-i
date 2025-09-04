#include <stdio.h>                //TOPO : ferramentas para funcionamento do codgo: stdio.h para comandos de entrada e saida
#include <string.h>               //+ string.h para manipulação total de dados strings 


struct Produto {                  // ABAIXO DO TOPO : inicio do codigo: Começa criantdo uma estrutura com nomes e tipos de dados
    char nome[50]; 
    int COD;
    float preco;
    int quantidade;
};


void cadastrarProduto(struct Produto *p, char nome[], int COD, float preco, int quantidade) { //+ depois cria função que armazeza esses dados 
    strcpy(p->nome, nome);   
    p->COD = COD;
    p->preco = preco;
    p->quantidade = quantidade;  	
}


void mostrarProduto(struct Produto p) {        // +Funçãp esclusiva para mostrar os dados
    printf("\n--- Produto ---\n");
    printf("Nome: %s\n", p.nome);
    printf("Codigo: %d\n", p.COD);
    printf("Preço: R$ %.2f\n", p.preco);
    printf("Quantidade: %d\n", p.quantidade);
}

int main() {                                  // CENTRO + tratamento de dados 
    struct Produto prod1;                     // + declaração de struct com nome do produto de Prod1(mais pode ser qualquer nome)

    printf("Digite o nome do produto: ");
    scanf(" %[^\n]", prod1.nome);

    printf("Digite o codigo: ");
    scanf("%d", &prod1.COD);

    printf("Digite o preco: ");
    scanf("%f", &prod1.preco);

    printf("Digite a quantidade: ");
    scanf("%d", &prod1.quantidade);

    mostrarProduto(prod1);                 // BASE DA TORRE : o que sera mostrado pro usuaario: Chama a função para mostrar produto cadastrado    

    return 0;
}





