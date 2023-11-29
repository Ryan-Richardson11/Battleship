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
                if (grid[i][j].equals(" ") || grid[i][j].equals("S")) {
                    System.out.print(" . |");
                } else {
                    System.out.print(" " + grid[i][j] + " |");
                }
            }
            System.out.println();
            System.out.println("  +---+---+---+---+---+---+---+---+---+---+");
        }
    }

    public void setUpBoard() {
        Random random = new Random();
        int randomShips = 0;
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = ".";
            }
        }
        while (randomShips < numShips) {
            int randomRow = random.nextInt(gridSize);
            int randomColumn = random.nextInt(gridSize);
            if (grid[randomRow][randomColumn].equals(".")) {
                grid[randomRow][randomColumn] = "S";
                randomShips += 1;
            }
        }
    }

    public void hitOrmiss(int row, int column) {
        if (grid[row][column] == "S") {
            System.out.println("Hit!");
            grid[row][column] = "X";
        } else {
            System.out.println("Miss!");
            grid[row][column] = "O";
        }
    }

    public boolean isGameOver() {
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                if (grid[i][j].equals("S")) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        BattleshipJAVA game = new BattleshipJAVA();
        game.initializeBoard();
        game.setUpBoard();
        while (game.isGameOver() == false) {
            try {
                game.drawBoard();
                System.out.println("Please enter a row from 0-9: ");
                int row = input.nextInt();
                System.out.println("Please enter a column from 0-9: ");
                int column = input.nextInt();
                game.hitOrmiss(row, column);
            } catch (Exception e) {
                System.out.println("Sorry that is invalid, please enter a value from 0-9");
            }
        }
    }
}