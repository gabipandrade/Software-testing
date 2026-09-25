package v4;

import java.util.Scanner;

public class Boliche {
    // aceita jogada extra no final
    
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
        int frame = 1;
        int jogadaIndex = 0;
        
        while (frame <= 10 && jogadaIndex < jogadas.length) {
            if (frame < 10) {
                // Frames 1-9: regras normais
                if (jogadas[jogadaIndex].equals("X")) {
                    // Strike
                    total += 10;
                    if (jogadaIndex + 1 < jogadas.length) {
                        total += getValor(jogadas[jogadaIndex + 1], 0);
                        if (jogadaIndex + 2 < jogadas.length) {
                            int valorAnterior = jogadas[jogadaIndex + 1].equals("/") ? 0 : getValor(jogadas[jogadaIndex + 1], 0);
                            total += getValor(jogadas[jogadaIndex + 2], valorAnterior);
                        }
                    }
                    jogadaIndex++;
                } else {
                    // Primeira jogada do frame
                    int primeira = getValor(jogadas[jogadaIndex], 0);
                    total += primeira;
                    jogadaIndex++;
                    
                    if (jogadaIndex < jogadas.length) {
                        if (jogadas[jogadaIndex].equals("/")) {
                            // Spare
                            total += (10 - primeira);
                            if (jogadaIndex + 1 < jogadas.length) {
                                total += getValor(jogadas[jogadaIndex + 1], 0);
                            }
                        } else {
                            // Segunda jogada normal
                            total += getValor(jogadas[jogadaIndex], primeira);
                        }
                        jogadaIndex++;
                    }
                }
            } else {
                // 10º frame: pode ter jogadas extras
                if (jogadas[jogadaIndex].equals("X")) {
                    // Strike no 10º frame
                    total += 10;
                    jogadaIndex++;
                    
                    // Duas jogadas extras
                    if (jogadaIndex < jogadas.length) {
                        total += getValor(jogadas[jogadaIndex], 0);
                        jogadaIndex++;
                        
                        if (jogadaIndex < jogadas.length) {
                            int valorAnterior = jogadas[jogadaIndex - 1].equals("/") ? 0 : getValor(jogadas[jogadaIndex - 1], 0);
                            total += getValor(jogadas[jogadaIndex], valorAnterior);
                            jogadaIndex++;
                        }
                    }
                } else {
                    // Primeira jogada do 10º frame
                    int primeira = getValor(jogadas[jogadaIndex], 0);
                    total += primeira;
                    jogadaIndex++;
                    
                    if (jogadaIndex < jogadas.length) {
                        if (jogadas[jogadaIndex].equals("/")) {
                            // Spare no 10º frame
                            total += (10 - primeira);
                            jogadaIndex++;
                            
                            // Uma jogada extra
                            if (jogadaIndex < jogadas.length) {
                                total += getValor(jogadas[jogadaIndex], 0);
                                jogadaIndex++;
                            }
                        } else {
                            // Segunda jogada normal no 10º frame
                            total += getValor(jogadas[jogadaIndex], primeira);
                            jogadaIndex++;
                        }
                    }
                }
            }
            frame++;
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