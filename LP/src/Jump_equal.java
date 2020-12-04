public class Jump_equal extends Instrucao_salto {
    String etiqueta;
    public Jump_equal(String i){
        etiqueta=i;
    }
    public void executa(TISC maq){
        int valor2=maq.getAval_pilha().pop();
        int valor1=maq.getAval_pilha().pop();
        if(valor1==valor2){
            jump(maq,etiqueta);
        }
        else{maq.incrementaPC();}
    }
    public String toString()
    {
        return "JEQ";
    }
}
