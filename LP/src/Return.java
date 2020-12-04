public class Return extends Instrucao_chamada_funcoes {
    public void executa(TISC maq){
        RegistoAtivacao temp=maq.getExec_memory().pop();
        //RegistoAtivacao temp=maq.getEP();
        maq.setPC(temp.getEnderecoRetorno());
        //maq.setEP(temp.getAccessLink());
        if(!maq.getExec_memory().isEmpty()) {
            maq.setEP(maq.getExec_memory().peek());
        }
        //System.out.println("Acaba: "+temp+" Return to:"+temp.getAccessLink());
    }
    public String toString()
    {
        return "RETURN";
    }
}
