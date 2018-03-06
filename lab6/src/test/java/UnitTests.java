import org.junit.*;

import static junit.framework.TestCase.assertEquals;

public class UnitTests {

    @Test
    public void boardHas9ActiveFields(){
        GameLogic gameLogic = new GameLogic();
        Board gameboard = gameLogic.CreateBoard();

        int boardRows = 3;
        int boardColumns = 3;

        for(int i = 0; i < boardRows; i++){
            for (int j = 0; j < boardColumns; j++) {
                assertEquals(false, gameboard.SpaceInUse(i,j));
            }
        }
    }

    @Test
    public void currentPlayerIsX(){
        GameLogic gameLogic = new GameLogic();

        assertEquals('X', gameLogic.CurrentPlayer().Symbol);
    }

    @Test
    public void currentPlayerIsO(){
        GameLogic gameLogic = new GameLogic();
        gameLogic.ChangePlayer();

        assertEquals('O', gameLogic.CurrentPlayer().Symbol);
    }


    @Test
    public void currentPlayerPlacesX(){
        GameLogic gameLogic = new GameLogic();
        Board gameBoard = gameLogic.CreateBoard();

        int placementRow = 0;
        int placementColumn = 0;
        gameLogic.makeMove(placementRow, placementColumn);

        assertEquals('X', gameBoard.SpaceSymbol(placementRow, placementColumn));
    }

    @Test
    public void currentPlayerPlacesO(){
        GameLogic gameLogic = new GameLogic();
        Board gameBoard = gameLogic.CreateBoard();

        int placementRow = 0;
        int placementColumn = 0;

        gameLogic.ChangePlayer();
        gameLogic.makeMove(placementRow, placementColumn);

        assertEquals('O', gameBoard.SpaceSymbol(placementRow, placementColumn));
    }

    @Test
    public void placementUnoccupied(){
        GameLogic gameLogic = new GameLogic();
        Board gameBoard = gameLogic.CreateBoard();

        int placementRow = 0;
        int placementColumn = 0;

        assertEquals(false, gameBoard.SpaceInUse(placementRow, placementColumn));
    }
}
