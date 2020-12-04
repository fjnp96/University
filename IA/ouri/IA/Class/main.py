import sys
from tabuleiro import *
from alfa_beta import *
from q_learning import *
def main():
    sys.setrecursionlimit(10000)
    estado_inicial=[2,0,0,5,3,1,1,5,1,0,0,0]
    print(sys.getrecursionlimit())
    print ("Start")
    print("Escolha o numero da opção")
    print("1-PvP")
    print("teste-para teste")
    opcao=input("Opção:")
    print(opcao)
    if(opcao=="1"):
        jogo=tabuleiro(estado_inicial)
        ciclo_pvp(jogo)
    if(opcao=="teste"):
        agent=q_learning()
        
def ciclo_pvp(jogo):
    #profundidade=5#profundidade do minmax
    print ("Start pvp")
    while(True):
        jogo.print_estado()
        if(jogo.a_jogar%2!=0):
            print("É a sua vez Jogador 1")
        else:
            print("É a sua vez Jogador 2")
        """
        score, move = alfa_beta(jogo,4,jogo.a_jogar)
        print("Jogada recomendada: ",end="")
        print(move+1)
        print("diferença de score: ",end="")
        print(score)
        """  
        jogada = int(input("Faça a sua jogada[1-6]:"))
        jogada-=1
        tuplo=jogo.move(jogada)#(estado,True)->Fez jogada
        while(tuplo==False):#(estado,False)->jogada invalida
            print("jogada não pode ser efectuada")
            jogada = int(input("Faça a sua jogada[1-6]:"))
            jogada-=1
            tuplo=jogo.move(jogada)
        
        fim=jogo.fim_jogo()
        if(fim!=False):
            if(fim==1):
                print("Jogador 1 ganhou")
            elif(fim==2):
                print("Jogador 2 ganhou")
            elif(fim==-1):
                print("empate")
            break
        jogo.vira_tabuleiro()
    
if __name__ == "__main__":
    main()
