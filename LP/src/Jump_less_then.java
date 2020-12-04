public class Jump_less_then extends Instrucao_salto{
    String etiqueta;
    public Jump_less_then(String i){
        etiqueta=i;
    }
    public void executa(TISC maq){
        int A=maq.getAval_pilha().pop();
        int B=maq.getAval_pilha().pop();
        if(B<A){
            jump(maq,etiqueta);
        }
        else{maq.incrementaPC();}
    }
    public String toString()
    {
        return "JLT";
    }
}
