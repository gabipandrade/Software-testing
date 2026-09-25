package v3;

import java.util.Scanner;

public class Boliche {
    // aceita strike e - para jogada não feita, o spare continua funcionando
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite as jogadas (números, X para strike, / para spare, - para miss), separados por espaço:");
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
            if (jogadas[i].equals("X")) {
                // Strike: 10 pontos + bônus das próximas duas jogadas
                total += 10;
                
                // Adiciona bônus das próximas duas jogadas se existirem
                if (i + 1 < jogadas.length) {
                    total += getValor(jogadas[i + 1], 0);
                    if (i + 2 < jogadas.length) {
                        int valorAnterior = jogadas[i + 1].equals("/") ? 0 : getValor(jogadas[i + 1], 0);
                        total += getValor(jogadas[i + 2], valorAnterior);
                    }
                }
                anterior = 10;
            } else if (jogadas[i].equals("/")) {
                // Spare: 10 pontos + bônus da próxima jogada
                int valorSpare = 10 - anterior;
                total += valorSpare;
                
                // Adiciona bônus da próxima jogada se existir
                if (i + 1 < jogadas.length) {
                    total += getValor(jogadas[i + 1], 0);
                }
                anterior = 0;
            } else {
                int valor = getValor(jogadas[i], anterior);
                total += valor;
                anterior = valor;
            }
        }
        return total;
    }
    
    private static int getValor(String jogada, int anterior) {
        if (jogada.equals("-")) {
            return 0;
        } else if (jogada.equals("X")) {
            return 10;
        } else if (jogada.equals("/")) {
            return 10 - anterior;
        } else {
            return Integer.parseInt(jogada);
        }
    }
}