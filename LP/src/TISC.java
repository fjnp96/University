
// Tiny Instruction Set Computer
import java.util.*;

public class TISC {
	ArrayList<Instrucao> ins_memory;
	Stack<Integer> aval_pilha;
	Stack<RegistoAtivacao> exec_memory;
	Hashtable<String,Integer> etiquetas;
	RegistoAtivacao EP;
	int PC;
	ArrayList<Integer> argumentos;
	/** Executa o programa TISC carregado na maquina. */
	public TISC(){
		ins_memory = new ArrayList<Instrucao>();
		aval_pilha = new Stack<Integer>();
		exec_memory = new Stack<RegistoAtivacao>();
		etiquetas = new Hashtable<String,Integer>();
		argumentos = new ArrayList<Integer>();

	}
	public void executa()
	{
		//int i= 0;
		PC=etiquetas.get("program");
		EP=new RegistoAtivacao("program");
		exec_memory.push(EP);
		System.out.println("Humildade!");
		while(!exec_memory.isEmpty()){
			//System.out.println("a executar: "+ins_memory.get(PC).toString());
			ins_memory.get(PC).executa(this);
			//System.out.println("pilha:"+aval_pilha.toString());
			/*
			if(i==20){
				break;
			}
			i++;
			 */
		}
		/*
		while(!aval_pilha.empty()){
			System.out.println(aval_pilha.pop());
		}
		*/
	}

	public int getPC() {
		return PC;
	}
	public void setPC(int PC){this.PC=PC;}
	public void incrementaPC(){PC++;}
	public RegistoAtivacao getEP() {
		return EP;
	}
	public void setEP(RegistoAtivacao EP){this.EP=EP;}

	public ArrayList<Instrucao> getIns_memory(){return ins_memory;}

	public Stack<Integer> getAval_pilha() {
		return aval_pilha;
	}
	public Hashtable<String, Integer> getEtiquetas() {return etiquetas;}

	public Stack<RegistoAtivacao> getExec_memory(){
		return exec_memory;
	}

	public ArrayList<Integer> getArgumentos() {
		return argumentos;
	}
}
