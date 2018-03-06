public class Board {
    private Field[][] Field;
    private int row;
    private int column;

    public Board(int row, int column){
        this.row = row;
        this.column = column;

        Field = new Field[this.row][this.column];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                Field[i][j] = new Field();
            }
        }
    }

    public void PlacePlayer(Player player, int x, int y){
        Field[x][y].Occupant = player;
    }

    public boolean SpaceInUse(int x, int y){
        return Field[x][y].Occupant != null;
    }

    public char SpaceSymbol(int x, int y){
        return Field[x][y].Occupant.Symbol;
    }
}
