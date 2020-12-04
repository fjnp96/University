public class Mult extends Instrucao_aritmetica {
    public void executa(TISC maq){
        int[] valores=getValores(maq);
        maq.getAval_pilha().push(valores[0]*valores[1]);
        maq.incrementaPC();
    }
    public String toString(){
        return "MULT";
    }
}
