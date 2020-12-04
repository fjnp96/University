from tabuleiro import *
import tabuleiro
from copy import *
#player é 1 ou 2
#N->profundidade da pesquisa
INFINITY = 1.0e400
def alfa_beta(tabuleiro,N,player):
    jogada=-1
    alfa=-INFINITY
    beta=INFINITY
    score= -INFINITY
    if tabuleiro.fim_jogo():
        return (-1,-1)
    for i in range(6):
        new_tabuleiro = deepcopy(tabuleiro)#para nao estragar o tabuleiro
        move=new_tabuleiro.move(i)
        if(move!=False):
            if(new_tabuleiro.joga_outra_vez()):
                s = max_alfa_beta(new_tabuleiro,N-1,player,alfa,beta)
            else:    
                new_tabuleiro.vira_tabuleiro()
                s = min_alfa_beta(new_tabuleiro,N-1,player,alfa,beta)
            if(s>score):
                jogada = i
                score = s
            alfa = max(score,alfa)
            return score, jogada
        else:
            continue
    return score, move

def min_alfa_beta(tabuleiro,N,player,alfa,beta):
    if(tabuleiro.fim_jogo()):
        return avalia(tabuleiro,player)
    if(N==0):
        return avalia(tabuleiro,player)
    score = INFINITY
    for i in range(6):
        new_tabuleiro = deepcopy(tabuleiro)#para nao estragar o tabuleiro
        move=new_tabuleiro.move(i)
        if(move!=False):
            if(new_tabuleiro.joga_outra_vez()):
                print("min repeat")
                score = min_alfa_beta(new_tabuleiro,N-1,player,alfa,beta)
            else:    
                new_tabuleiro.vira_tabuleiro()
                #o novo score é o minimo entre o antigo e o max do oponente
                score = min(score,max_alfa_beta(new_tabuleiro,N-1,player,alfa,beta))
            if(score<=alfa):
                return score
            beta = min(beta,score)
        else:continue
    return score

def max_alfa_beta(tabuleiro,N,player,alfa,beta):
    if(tabuleiro.fim_jogo()):
        return avalia(tabuleiro,player)
    if(N==0):
        return avalia(tabuleiro,player)
    score = -INFINITY
    for i in range(6):
        new_tabuleiro = deepcopy(tabuleiro)#para nao estragar o tabuleiro
        move=new_tabuleiro.move(i)
        if(move!=False):
            #caso o jogador jogue outra vez
            if(new_tabuleiro.joga_outra_vez()):
                print("max repeat")
                score = max_alfa_beta(new_tabuleiro,N-1,player,alfa,beta)
            else:    
                new_tabuleiro.vira_tabuleiro()
                #o novo score é o minimo entre o antigo e o max do oponente
                score = max(score,min_alfa_beta(new_tabuleiro,N-1,player,alfa,beta))
            if(score>=beta):
                return score
            alfa = max(alfa,score)
        else:continue
    return score
#recebe a class tabuleiro e o jogador e retorna os pontos dele
def avalia(tabuleiro,player):
    if(player%2!=0):
        return tabuleiro.p1-tabuleiro.p2
    else:
        return tabuleiro.p2-tabuleiro.p1
                
            
    
    
    
