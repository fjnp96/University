public class Push_INT extends Instrucao_manipulacao_inteiros{
    int val;

    public Push_INT(int i)
    {
        val = i;
    }
    public void executa(TISC maq)
    {
        maq.getAval_pilha().push(val);
        maq.incrementaPC();
    }
    public String toString()
    {
        return "PUSH_INT " + Integer.toString(val);
    }


}
