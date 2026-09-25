import java.util.Scanner;

public class Boliche {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int[] jogadas = new int[20];
            
            System.out.println("Digite 20 números (pinos derrubados em cada jogada):");
            
            // Recebe os 20 números
            for (int i = 0; i < 20; i++) {
                System.out.print("Jogada " + (i + 1) + ": ");
                jogadas[i] = scanner.nextInt();
            }
            
            // Calcula a pontuação total
            int pontuacaoTotal = computaPlacar(jogadas);
            System.out.println("Pontuação total: " + pontuacaoTotal);
        }
    }

    static int computaPlacar(int[] jogadas) {
        int pontuacaoTotal = 0;
        for (int jogada : jogadas) {
            pontuacaoTotal += jogada;
        }
        return pontuacaoTotal;
    }

}