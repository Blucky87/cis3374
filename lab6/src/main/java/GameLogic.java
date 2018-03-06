import java.util.ArrayDeque;
import java.util.Queue;

public class GameLogic {
    private Queue<Player> playerList;
    private Board gameBoard;

    public GameLogic(){
        CreateBoard();
        playerList = new ArrayDeque<>();
        playerList.add(new Player('X'));
        playerList.add(new Player('O'));
    }

    public Board CreateBoard(){
        gameBoard = new Board(3,3);

        return gameBoard;
    }

    public Player CurrentPlayer(){
        return  playerList.peek();
    }

    public void ChangePlayer(){
        playerList.add(playerList.poll());
    }

    public void makeMove(int x, int y){
        gameBoard.PlacePlayer(CurrentPlayer(), x, y);
        ChangePlayer();
    }

}
