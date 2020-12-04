public class Exp extends Instrucao_aritmetica{
    @Override
    public void executa(TISC maq) {
        int[] valores=getValores(maq);
        maq.getAval_pilha().push((int) Math.pow( valores[0],valores[1]));
        maq.incrementaPC();
    }
    public String toString()
    {
        return "EXP";
    }
}
