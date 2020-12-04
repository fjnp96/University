public class Locals extends Instrucao_chamada_funcoes{
    int argumentos;
    int variaveis;
    public Locals(String i,String j){
        argumentos=Integer.parseInt(i);
        variaveis=Integer.parseInt(j);
    }
    public void executa(TISC maq) {
        if(variaveis>0) {
            maq.getEP().setVars(new int[variaveis]);
        }
        if(argumentos>0) {
            int args[] = new int[argumentos];
            int i = 0;
            while (i < argumentos) {
                args[i] = maq.getArgumentos().get(i);
                i++;
            }
            maq.getEP().setArgs(args);
            maq.getArgumentos().clear();
        }
        maq.incrementaPC();
    }
    public String toString()
    {
        return "LOCALS "+ Integer.toString(argumentos) +" "+Integer.toString(variaveis);
    }
}
