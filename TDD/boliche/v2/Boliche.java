package v2;

import java.util.Scanner;

public class Boliche {
//aceita spare
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite as jogadas (números e / para spare), separados por espaço:");
        String input = scanner.nextLine();
        String[] jogadas = input.split(" ");

        int total = computaPlacar(jogadas);
        System.out.println("Total: " + total);

        scanner.close();
    }
    public static int computaPlacar(String[] jogadas) {
        int total = 0;
        int anterior = 0;
        
        for (int i = 0; i < jogadas.length; i++) {
            if (jogadas[i].equals("/")) {
                // Spare: soma 10 pontos + bônus da próxima jogada
                int valorSpare = 10 - anterior;
                total += valorSpare;
                
                // Adiciona bônus da próxima jogada se existir
                if (i + 1 < jogadas.length) {
                    if (jogadas[i + 1].equals("/")) {
                        total += 10 - Integer.parseInt(jogadas[i]);
                    } else {
                        total += Integer.parseInt(jogadas[i + 1]);
                    }
                }
            } else {
                int valor = Integer.parseInt(jogadas[i]);
                total += valor;
                anterior = valor;
            }
        }
        return total;
    }
    
    // Método auxiliar para manter compatibilidade com array de inteiros
    public static int computaPlacar(int[] jogadas) {
        int total = 0;
        for (int i = 0; i < jogadas.length; i++) {
            total += jogadas[i];
        }
        return total;
    }
}