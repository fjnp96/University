public class Store_VAR extends Instrucao_acesso_variaveis {
    int distancia;
    int numero;

    public Store_VAR(String i, String j)
    {
        distancia = Integer.parseInt(i);
        numero = Integer.parseInt(j);
    }

    public String toString()
    {
        return "STORE_VAR " + distancia + " " + numero;
    }

    public void executa(TISC maq)
    {
        int i=0;
        RegistoAtivacao temp=maq.getEP();
        while(i<distancia){
            temp=temp.getAccessLink();
            i++;
        }
        temp.getVars()[numero-1]=maq.getAval_pilha().pop();
        maq.incrementaPC();
    }
}
