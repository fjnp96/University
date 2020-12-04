public class Print_ln extends Instrucao_saida {
    public void executa(TISC maq){
        System.out.println();
        maq.incrementaPC();
    }
    public String toString()
    {
        return "PRINT_LN";
    }
}
