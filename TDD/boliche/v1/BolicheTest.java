import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class BolicheTest {

    @Test
    public void testPlacarSimples() {
        int[] jogadas = {1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int resultado = Boliche.computaPlacar(jogadas);
        assertEquals(15, (int) resultado);
    }

    @Test
    public void testPlacarTodosZeros() {
        int[] jogadas = new int[20]; // todos zeros
        int resultado = Boliche.computaPlacar(jogadas);
        assertEquals(0, (int) resultado);
    }

    @Test
    public void testPlacarMaximo() {
        int[] jogadas = new int[20];
        for (int i = 0; i < 20; i++) {
            jogadas[i] = 10;
        }
        int resultado = Boliche.computaPlacar(jogadas);
        assertEquals(200, (int) resultado);
    }
}
