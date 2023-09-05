import java.util.Scanner;

public class BattleshipJAVA {
    int gridSize = 10;
    String[][] grid = new String[gridSize][gridSize];
    int numShips = 5;
    String columnList = "    0   1   2   3   4   5   6   7   8   9";

    public void createGrid() {
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = "";
            }
        }
    }

    public void drawBoard() {
        System.out.println(columnList);
        System.out.println("  +---+---+---+---+---+---+---+---+---+---+");
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                System.out.println(" " + grid[i][j] + " |");
                System.out.println("  +---+---+---+---+---+---+---+---+---+---+");
            }
        }
    }

    public static void main(String[] args) {
        drawBoard();
    }

}
