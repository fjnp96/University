public class Store_ARG  extends Instrucao_acesso_argumentos{
    int distancia;
    int numero;

    public Store_ARG(String i, String j)
    {
        distancia = Integer.parseInt(i);
        numero = Integer.parseInt(j);
    }

    public String toString()
    {
        return "STORE_ARG " + distancia + " " + numero;
    }

    public void executa(TISC maq)
    {
        int i=0;
        RegistoAtivacao temp=maq.getEP();
        while(i<distancia){
            temp=temp.getAccessLink();
            i++;
        }
        temp.getArgs()[numero-1]=maq.getAval_pilha().pop();
        maq.incrementaPC();
    }
}
