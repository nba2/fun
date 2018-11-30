// An implementation of a Turing Machine
// (c) 2018

import structure5.Vector;

public class Machine {
    private String tape;                 // a finite portion of "infinite" tape
    private int pos;                     // where the tape head is positioned
    private int state;                   // machine's internal state
    private Vector<Instruction> program; // a program

    public Machine(String tape, int pos, int state)
    // construct a machine with an initial tape fragment, a head position,
    // and initial state.
    {
	this.tape = tape;
	this.pos = pos;    // assume 0 <= pos < tape.length()
	this.state = state;
	// the program is initially empty
	this.program = new Vector<Instruction>();
    }

    public void setProgram(Instruction[] p)
    // change the program on the machine
    {
	// iteration across the array, filling the vector
	for (Instruction i : p) {
	    program.add(i);
	}
    }

    public int state()
    // accessor for the state
    {
	return state;
    }

    public char symbol()
    // accessor ("getter") for the current symbol under the tape head.
    {
	return tape.charAt(pos);
    }

    private void write(char c)
    // mutator ("setter") method for current symbol under the tape head
    {
	tape = tape.substring(0,pos) + c + tape.substring(pos+1); // ugh
    }

    private void move(int change)
    // slide the tape left or right (assumes abs(change) == 1)
    {
	pos = pos + change;
	if (pos < 0) {
	    tape = '0'+tape;
	    pos++;
	}
	if (pos == tape.length()) {
	    tape = tape + '0';
	}
    }

    public Instruction instruction()
    // get the instruction that currently matches the state & symbol, or null
    {
	Instruction pattern = new Instruction(state(),symbol(), // ignore:
					      '!',0,0);
	int i = program.indexOf(pattern);
	if (i >= 0) {
	    return program.get(i);
	} else {
	    return null;
	}
    }

    public boolean halted()
    // returns true if the machine is currently halted
    {
	return instruction() == null;
    }

    public void step()
    // execute an instruction, if not halted.
    {
      Instruction i = instruction();
      if (i != null) {
        write(i.newSymbol());
        move(i.movement());
        state = i.newState();
      }
    }

    public void go()
    // reset and run until machine halts (doesn't print intermediate states)
    {
	state = 1;
	while (!halted()) { step(); }
    }

    public String toString()
    // print machine (tape and location of tape head)
    {
	String result = "..." + tape + "...\n   ";
	for (int i = 0; i < pos; i++) {
	    result += " ";
	}
	result += "^[" + state + "]";
	return result;
    }

    public static void main(String[] args)
    {
	System.out.println(args);
	Machine m = new Machine(args.length > 1 ? args[1] : "0",0,1);
	System.out.println(m);
    }
}
