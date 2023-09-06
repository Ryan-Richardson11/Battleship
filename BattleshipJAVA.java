import java.util.Scanner;

public class BattleshipJAVA {
    int gridSize = 10;
    String[][] grid = new String[gridSize][gridSize];
    {
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = "";
            }
        }
    }
    int numShips = 5;
    String columnList = "    0   1   2   3   4   5   6   7   8   9";

    public void drawBoard() {
        System.out.println(columnList);
        System.out.println("  +---+---+---+---+---+---+---+---+---+---+");

        for (int i = 0; i < gridSize; i++) {
            System.out.println(i + " |");
            for (int j = 0; j < gridSize; j++) {
                System.out.println(" " + grid[i][j] + " |");
            }
            System.out.println("  +---+---+---+---+---+---+---+---+---+---+");
        }
    }

    public static void main(String[] args) {
        BattleshipJAVA game = new BattleshipJAVA();
        game.drawBoard();
    }

}
