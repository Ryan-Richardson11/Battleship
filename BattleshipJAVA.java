import java.util.Scanner;
import java.util.Random;

public class BattleshipJAVA {
    int gridSize = 10;
    String[][] grid = new String[gridSize][gridSize];
    String column_list = "    0   1   2   3   4   5   6   7   8   9";
    int numShips = 5;

    public void initializeBoard() {
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = " ";
            }
        }
    }

    public void drawBoard() {
        System.out.println(column_list);
        System.out.println("  +---+---+---+---+---+---+---+---+---+---+");

        for (int i = 0; i < gridSize; i++) {
            System.out.print(i + " |");
            for (int j = 0; j < gridSize; j++) {
                System.out.print(" " + grid[i][j] + " |");
            }
            System.out.println();
            System.out.println("  +---+---+---+---+---+---+---+---+---+---+");
        }
    }

    public void setUpBoard() {
        int randomShips = 0;
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = ".";
            }
        }
        while (randomShips > numShips) {
            randomRow = 
            randomColumn = 
            if (grid[randomRow][randomColumn] != "S") {
                grid[randomRow][randomColumn] == "S"
                randomShips += 1;
            }
        }
    }

    public static void main(String[] args) {
        BattleshipJAVA game = new BattleshipJAVA();
        game.initializeBoard();
        game.drawBoard();
        game.setUpBoard();
    }
}