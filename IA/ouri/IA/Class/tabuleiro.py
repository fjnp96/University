from alfa_beta import *
INFINITY = 1.0e400
class tabuleiro:
    def __init__(self,tabuleiro):
        self.a_jogar=1
        self.p1=0
        self.p2=0
        self.tabuleiro=tabuleiro
        self.historico={}
    def move(self,jogada):
        tabuleiro=self.tabuleiro.copy()
        if(self.a_jogar%2!=0):
            p1 = self.p1
            p2 = self.p2
        else:
            p1=self.p2
            p2=self.p1
        if(not self.verifica_jogada(jogada)):
            #print("jogada não pode ser efectuada")
            return False
        nr_pecas = tabuleiro[jogada]
        pointer=jogada
        pointer+=1
        while(nr_pecas>0):
            if(pointer==12):
                pointer=0
                continue
            if(pointer==jogada):
                pointer+=1
                continue
            tabuleiro[pointer]+=1
            pointer+=1;
            nr_pecas-=1
        tabuleiro[jogada]=0
        pointer-=1
        if(pointer>5 and (tabuleiro[pointer]==2 or tabuleiro[pointer]==3)):
            print("a comer")
            while(pointer>5 and (tabuleiro[pointer]==2 or tabuleiro[pointer]==3)):
                print("come na posicao",end="")
                print(pointer)
                p1+=tabuleiro[pointer]
                tabuleiro[pointer]=0
                pointer-=1
        self.tabuleiro=tabuleiro
        self.p1=p1
        self.p2=p2
        return True
    #verifica se o jogardor joga outra vez ou nao
    def joga_outra_vez(self):
        if(self.tabuleiro_vazio()):
            return True
        else:return False
        
    def fim_jogo(self):
        self.lida_com_ciclo()#verifica os ciclos
        
        if(self.p1>=25):
            return 1
        elif(self.p2>=25):
            return 2
        jogada=0
        while(jogada<6):#verifica se é possivel para o p1 jogar
            if(self.verifica_jogada(jogada)):
                return False
            jogada+=1
        self.vira_tabuleiro()
        jogada=0
        while(jogada<6):#verifica se é possivel para o p2 jogar
            if(self.verifica_jogada(jogada)):
                self.vira_tabuleiro()
                return False
            jogada+=1
        self.recolhe_tabuleiro()
        if(self.p1>self.p2):
            return 1
        elif(self.p2>self.p1):
            return 2
        else:
            return -1

    #usa historico para ver se o estado ja foi visitado previamente
    def lida_com_ciclo(self):
        if(str(self.tabuleiro) in self.historico.keys()):#ciclo
            print("recolhe tabuleiro")
            self.recolhe_tabuleiro()
        else:
            #adiciona o tabuleiro ao historico
            self.historico.update({str(self.tabuleiro):1})
            
    #verifica se a jogada pode ser efectuada
    def verifica_jogada(self,jogada):
        estado=self.tabuleiro.copy()
        if(jogada<0 or jogada>5 or estado[jogada]==0):
            return False
        elif(estado[jogada]==1):
            for i in range(6):
                if(estado[i]>1 and i!=jogada):
                    return False
        elif(self.tabuleiro_vazio() and jogada+estado[jogada]<6):
            return False
        return True
    
    #tabuleiro vazio do lado do oponente
    def tabuleiro_vazio(self):
        estado=self.tabuleiro.copy()
        for i in range(6,12):
            if(estado[i]>0):
                return False
        return True
    #vira o tabuleiro e encrementa o a_jogar
    def vira_tabuleiro(self):
        tabuleiro=self.tabuleiro.copy()
        t1=tabuleiro[len(tabuleiro)//2:]
        t2=tabuleiro[:len(tabuleiro)//2]
        self.a_jogar+=1
        self.tabuleiro=t1+t2

    #recolhe as peças restantes está em ciclo
    def recolhe_tabuleiro(self):
        print("recolhe")
        for i in range(6):
            if(self.a_jogar%2!=0):
                self.p1+=self.tabuleiro[i]
            else:
                self.p2+=self.tabuleiro[i]
            self.tabuleiro[i]=0
        for i in range(6,12):
            if(self.a_jogar%2!=0):
                self.p2+=self.tabuleiro[i]
            else:
                self.p1+=self.tabuleiro[i]
            self.tabuleiro[i]=0
        
    def print_estado(self):
        def printx(x):print(x,end=" ")
        printx("  ")
        for i in range(11,5,-1):
            printx(str(self.tabuleiro[i])+" ")
        print("")
        if(self.a_jogar%2!=0):
            printx(str(self.p2)+"                   ")
            print(self.p1)
        else:
            printx(str(self.p1)+"                   ")
            print(self.p2)        
        printx("  ")
        for i in range(6):
            printx(str(self.tabuleiro[i])+" ")
        print("")            
                    
                
                

