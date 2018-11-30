public class first {
    public static void main(String[] args)
    {
	int RIGHT=1;
	int LEFT=-1;
	Machine m = new Machine("0",0,1);
	Instruction[] hi = {
	    new Instruction(1,'0','H',RIGHT,2),
	    new Instruction(2,'0','e',RIGHT,3),
	    new Instruction(3,'0','l',RIGHT,4),
	    new Instruction(4,'0','l',RIGHT,5),
	    new Instruction(5,'0','o',RIGHT,6),
	    new Instruction(6,'0',',',RIGHT,7),
	    new Instruction(7,'0',' ',RIGHT,8),
	    new Instruction(8,'0','w',RIGHT,9),
	    new Instruction(9,'0','o',RIGHT,10),
	    new Instruction(10,'0','r',RIGHT,11),
	    new Instruction(11,'0','l',RIGHT,12),
	    new Instruction(12,'0','d',RIGHT,13),
	    new Instruction(13,'0','.',RIGHT,0),
	};
	m.setProgram(hi);
	System.out.println(m);
	while (!m.halted()) {
	    m.step();
	    System.out.println(m);
	}
    }
}
