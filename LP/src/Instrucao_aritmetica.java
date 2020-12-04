public abstract class Instrucao_aritmetica extends Instrucao {
    static int[] getValores(TISC maq){
        int[] valores = new int[2];
        valores[1]=maq.getAval_pilha().pop();
        valores[0]=maq.getAval_pilha().pop();
        return valores;
    }
}
