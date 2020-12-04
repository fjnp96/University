public class RegistoAtivacao {
    String nome;
    int[] args;
    int[] vars;

    int EnderecoRetorno;//inteiro do antigo PC
    RegistoAtivacao AccessLink;//aponta para o registo de ativacao anterior

    public RegistoAtivacao(String nome){
        this.nome=nome;
    }
    RegistoAtivacao getAccessLink(){return AccessLink;}
    int getEnderecoRetorno(){return EnderecoRetorno;}
    void setEnderecoRetorno(int enderecoRetorno){this.EnderecoRetorno=enderecoRetorno;};
    void setAccessLink(RegistoAtivacao controlLink){this.AccessLink=controlLink;};
    void setArgs(int[] args){this.args=args;}
    void setVars(int[] vars){this.vars=vars;}
    int[] getArgs(){return args;}
    int[] getVars(){return vars;}

    public String getNome() {
        return nome;
    }
    void print_args(){
        System.out.print("ARGUMENTOS: ");
        for(int i=0;i<args.length;i++){
            System.out.print(args[i]+" ");
        }
        System.out.println();
    }
}
