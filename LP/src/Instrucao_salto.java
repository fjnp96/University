public abstract class Instrucao_salto extends Instrucao{
    void jump(TISC maq,String etiqueta){
        maq.setPC(maq.getEtiquetas().get(etiqueta));
        //System.out.println("Saltou para "+etiqueta);
    }
}
