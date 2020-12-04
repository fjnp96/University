public class Call extends Instrucao_chamada_funcoes {
    int distancia;
    String etiqueta;
    public Call(String i,String j)
    {
        distancia = Integer.parseInt(i);
        etiqueta = j;
    }

    @Override
    public void executa(TISC maq) {
        RegistoAtivacao registo = new RegistoAtivacao(etiqueta);
        registo.setEnderecoRetorno(maq.getPC()+1);
        if(distancia==-1){
            registo.setAccessLink(maq.getEP());
        }
        else{
            int i= 0;
            RegistoAtivacao temp=maq.getEP().getAccessLink();
            while(i<distancia){
                temp=temp.getAccessLink();
                i++;
            }
            registo.setAccessLink(temp/*.getAccessLink()*/);
        }
        maq.getExec_memory().push(registo);
        maq.setPC(maq.getEtiquetas().get(etiqueta));
        maq.setEP(registo);
        //System.out.println("salta para o registo: "+registo.getNome()+" retorna para: "+registo.getAccessLink().getNome());
    }

    public String toString()
    {
        return "CALL "+ Integer.toString(distancia) +" "+etiqueta;
    }
}
