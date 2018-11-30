// A simple model for a 5-tuple holding a Turing Machine instruction.
public class Instruction {
    private int  state;		// state for matching instruction
    private char symbol;	// symbol on tape for matching
    private char newSymbol;	// the symbol *written* to tape
    private int  movement;	// the direction to move the "tape head"
    private int  newState;      // the new state

    public Instruction(int state, char symbol,
		       char newSymbol, int movement, int newState) {
	// construct instructions for reading, writing, moving the tape
	this.state = state;
	this.symbol = symbol;
	this.newSymbol = newSymbol;
	this.movement = movement;
	this.newState = newState;
    }

    // accessor methods for each instruction field
    public int state() { return state; }
    public char symbol() { return symbol; }
    public char newSymbol() { return newSymbol; }
    public int movement() { return movement; }
    public int newState() { return newState; }

    public boolean equals(Object other)
    // return true if two instructions match the same state & symbol ONLY
    {
	Instruction that = (Instruction)other;
	return this.state == that.state &&
	    this.symbol == that.symbol;
    }

    public String toString()
    // print an instruction
    {
	return "["+state+",'"+symbol+"','"+newSymbol+"',"+
	    (movement<0?"LEFT":"RIGHT")+","+newState+"]";
    }
}
