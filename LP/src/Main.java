
// Programa principal para a implementacaoo da maquina abstracta TISC.

public class Main {
  public static void main(String args[])
    throws Exception
  {
    parser aParser = new parser();
    TISC maquina;

    // carrega o programa TISC
    maquina = (TISC) aParser.parse().value;

    // e executa-o
    if (maquina != null)
      maquina.executa();
    /*
    System.out.println("//////////Instruções em memoria/////////\n");
    for (Instrucao s : maquina.ins_memory)
    {
      System.out.println(s.toString());
    }
     */
  }
}
