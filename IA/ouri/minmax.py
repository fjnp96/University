from ouri import *
def max_alfa_beta(estado,historico,alfa,beta,a_jogar):
    maxvalor=-50 #pior que o pior caso
    jogada=None

    fim=fim_jogo(estado,historico)

    if(fim!=False):
        vencedor=jogador_vencedor(fim,a_jogar)
        if(vencedor==1):
            return (0-estado[1],0)
        elif(vencedor==2):
            #print("Jogador 2 ganhou")
            return (estado[2],0)
        elif(vencedor==-1):
            return (0,0)
    temp=estado
    for i in range(6):
        (estado,joga)=move(estado,i)
        if(joga):
            estado=vira_tabuleiro(estado)
            a_jogar+=1
            (valor,j1) = min_alfa_beta(estado,historico,alfa,beta,a_jogar)
            if(valor>maxvalor):
                maxvalor=valor
                jogada=i
            estado=temp
            if(maxvalor>=beta):
                return (maxvalor,jogada)
            if(maxvalor>alfa):
                alfa=maxvalor
    return (maxvalor,jogada)

def min_alfa_beta(estado,historico,alfa,beta,a_jogar):
    minvalor=50 #pior que o pior caso
    jogada=None

    fim=fim_jogo(estado,historico)

    if(fim!=False):
        vencedor=jogador_vencedor(fim,a_jogar)
        if(vencedor==1):
            return (0-estado[1],0)
        elif(vencedor==2):
            #print("Jogador 2 ganhou")
            return (estado[2],0)
        elif(vencedor==-1):
            return (0,0)
    temp=estado
    for i in range(6):
        (estado,joga)=move(estado,i)
        if(joga):
            (valor,j1) = max_alfa_beta(estado,historico,alfa,beta,a_jogar)
            if(valor<minvalor):
                minvalor=valor
                jogada=i
            estado=temp
            if(minvalor<=alfa):
                return (minvalor,jogada)
            if(minvalor<beta):
                alfa=minvalor
    return (minvalor,jogada)
            
            
            
