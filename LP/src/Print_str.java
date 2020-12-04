public class Print_str extends Instrucao_saida {
    String str;
    public Print_str(String i){
        str=i;
    }
    public void executa(TISC maq){
        System.out.print(str);
        maq.incrementaPC();
    }
    public String toString()
    {
        return "PRINT_STR "+str;
    }
}
