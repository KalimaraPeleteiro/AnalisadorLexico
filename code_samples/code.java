package code_samples;

import java.util.Scanner;

// Comentário
public class code {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o primeiro número: ");
        double numero1 = scanner.nextDouble();

        System.out.println("Digite o segundo número: ");
        double numero2 = scanner.nextDouble();

        System.out.println("Digite o terceiro número: ");
        double numero3 = scanner.nextDouble();

        double media = calcularMedia(numero1, numero2, numero3);
        System.out.println("A média é: " + media);

        scanner.close();
    }

    public static double calcularMedia(double num1, double num2, double num3) {
        return (num1 + num2 + num3) / 3;
    }
}
