public class Set_ARG extends Instrucao_chamada_funcoes{
    int argumento;
    public Set_ARG(String i)
    {
        argumento = Integer.parseInt(i);
    }

    @Override
    public void executa(TISC maq) {
        //System.out.println("set_arg: "+maq.getAval_pilha().peek());
        maq.getArgumentos().add(argumento-1,maq.getAval_pilha().pop());
        maq.incrementaPC();
    }

    public String toString()
    {
        return "SET_ARG "+ Integer.toString(argumento);
    }
}
