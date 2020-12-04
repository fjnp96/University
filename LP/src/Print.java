public class Print extends Instrucao_saida {
    public void executa(TISC maq){
        System.out.print(maq.getAval_pilha().pop());
        maq.incrementaPC();
    }
    public String toString()
    {
        return "PRINT";
    }
}
