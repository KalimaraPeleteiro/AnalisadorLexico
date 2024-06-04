#include <stdio.h>

int main() {
    int num1, num2, soma;

    // Solicita ao usuário que insira o primeiro número
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    // Solicita ao usuário que insira o segundo número
    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    // Calcula a soma dos números
    soma = num1 + num2;

    // Imprime a soma
    printf("A soma de %d e %d é: %d\n", num1, num2, soma);

    return 0;
}