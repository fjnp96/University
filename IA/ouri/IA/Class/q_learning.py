#Q-leaning
import pickle #para escrever e ler objectos de ficheiros
import random
from tabuleiro import *

INFINITY = 1.0e400
alpha = 0.1
gamma = 0.6
epsilon = 0.1

class q_learning:
    def __init__(self,modo):
        #lê Q_table existente
        if(modo==1):
            self.q_table=load_q_table
        else:
            self.q_table={}
        self.historico=[]
        
    def load_q_table(self):
        f = open("q_table.pkl","rb")
        return pickle.load(f)

    def train_with_alfa_beta(self,tabuleiro):
        score1=tabuleiro.p1#guarda score antes da jogada
        old_tabuleiro=tabuleiro.tabuleiro.copy()#guarda o tabuleiro antes de jogar
        old_array=self.q_table.get(tabuleiro.tabuleiro).copy()
        #se ja existe este estado na q_table
        if(str(tabuleiro.tabuleiro) in self.q_table.keys()):
            #explorar aleatoriamente
            if(random.uniform(0, 1) < epsilon):
                jogada=random.randint(0,5)
                while(tabuleiro.move(jogada)==False):
                    jogada=random.randint(0,5)
            #explora os ja aprendidos
            else:
                #escolhe maximo dos Q_value
                jogada=max(self.q_table.get(str(tabuleiro.tabuleiro)))
        #caso ainda nao tenha passado por este estado
        #cria o estado com [str(tabuleiro):[0,0,0,0,0,0]]
        else:
            #mete jogadas impossiveis a False
            temp=[0,0,0,0,0,0]
            for i in range(6):#para cada jogada verifica as que sao impossiveis
                if(not(tabuleiro.verifica_jogada(i))):
                    temp[i]=-INFINITY#jogada possivel=-INFINITY
            self.q_table.update({str(tabuleiro.tabuleiro):temp.copy()})
            jogada=random.randint(0,5)
            while(tabuleiro.move(jogada)==False):
                jogada=random.randint(0,5)
        
        old_value=self.q_table.get(str(old_tabuleiro))[jogada]#old Q value
        score2=tabuleiro.p1#score depois da jogada
        reward=-25+score2-score1#calculo da reward em certa
        next_max=max(self.q_table.get(str(tabuleiro.tabuleiro)))#maximo next_Qvalue
        #calcula o novo Qvalue para o antigo tabuleiro
        new_value=(1-alpha)*old_value+alpha*(reward + gamma * next_max)
        old_array[jogada]=new_value
        #atualiza a q_table no antigo tabuleiro com o novo Qvalue
        self.q_table.update({str(old_Tabuleiro):old_array})



        """
        fim=tabuleiro.fim_jogo()
        if(fim!=False):
            if(fim==1):
                print("O agent ganhou")
            elif(fim==2):
                print("Jogador 2 ganhou")
            elif(fim==-1):
                print("empate")
            break
         """
                    
                
                
           
           
    
    
