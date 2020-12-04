public class Push_ARG extends Instrucao_acesso_variaveis{
    int distancia;
    int numero;

    public void executa(TISC maq) {
        int i=0;
        RegistoAtivacao temp=maq.getEP();
        while(i<distancia){
            temp=temp.getAccessLink();
            i++;
        }
        //System.out.println("push_arg:"+temp.getArgs()[numero-1]);
        maq.getAval_pilha().push(temp.getArgs()[numero-1]);
        maq.incrementaPC();
        //temp.print_args();
    }

    public Push_ARG(String i, String j)
    {
        distancia = Integer.parseInt(i);
        numero = Integer.parseInt(j);
    }
    public String toString()
    {
        return "PUSH_ARG " + distancia + " " + numero;
    }
}
