public class Jump extends Instrucao_salto{
    String etiqueta;
    public Jump(String i){
        etiqueta=i;
    }
    public void executa(TISC maq){
        jump(maq,etiqueta);
    }
    public String toString()
    {
        return "JUMP "+etiqueta;
    }
}
