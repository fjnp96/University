

def main():
	print ("Start")
	print("Escolha o numero da opção")
	print("1-PvP")
	opcao=input("Opção:")
	print("escolheu a opcao: "+str(opcao))
	if(opcao==1):
		ciclo_pvp()
	#estado_inicial = move(estado_inicial,5)
	

def ciclo_pvp():
	print ("Start pvp")
	a_jogar=1
	estado=([4,4,4,4,4,4,4,4,4,4,4,4],0,0)
	historico=[]
	while(True):
		if(a_jogar%2==0):
			lida_com_ciclo(estado[0],historico)
		jogada = input()
		jogada-=1
		estado=move(estado,jogada)
		if(a_jogar%2==0):
			lida_com_ciclo(estado[0],historico)
		fim=fim_jogo(estado)
		if(fim!=False):
			if(fim==1 and a_jogar%2!= 0):
				print("Jogador 1 ganhou")
			elif(fim==1 and a_jogar%2== 0):
				print("Jogador 2 ganhou")
			elif(fim==2 and a_jogar%2==0):
				print("Jogador 1 ganhou")
			elif(fim==2 and a_jogar%2!= 0):
				print("Jogador 2 ganhou")
			elif(fim==0):
				print("Empate")
			break
		estado=vira_tabuleiro(estado)
		a_jogar+=1


#recebe um tabuleiro para dicionar e verificar a sua existencia na lista
def lida_com_ciclo(tabuleiro,historico):
	if(any(list == tabuleiro for list in historico)): 
		print("estado ja visitado") 
	else: 
		historico.append(tabuleiro)
def move(estado,jogada):
	tabuleiro=estado[0]
	p1 = estado[1]
	p2 = estado[2]
	if(not verifica_jogada(tabuleiro,jogada)):
		print("jogada não pode ser efectuada")
		return
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
	print("pointer"+str(pointer))
	print(tabuleiro[pointer])
	if(pointer>5 and (tabuleiro[pointer]==2 or tabuleiro[pointer]==3)):
		while(pointer>5 and (tabuleiro[pointer]==2 or tabuleiro[pointer]==3)):
			p1+=tabuleiro[pointer]
			tabuleiro[pointer]=0
			pointer-=1
	return (tabuleiro,p1,p2)


def fim_jogo(estado):
	tabuleiro=estado
	if(tabuleiro[1]>=25):
		return 1
	elif(tabuleiro[2]>=25):
		return 2
	jogada=0
	while(jogada<6):#verifica se é possivel para o p1 jogar
		if(verifica_jogada(tabuleiro[0],jogada)):
			return False
		jogada+=1
	tabuleiro=vira_tabuleiro(tabuleiro)
	while(jogada<6):#verifica se é possivel para o p2 jogar
		if(verifica_jogada(tabuleiro[0],jogada)):
			return False
		jogada+=1
	pecas_p2=tabuleiro[1]
	pecas_p1=tabuleiro[2]
	for i in range(6):
		pecas_p2+=tabuleiro[0][i]
	for i in range(6,12):
		pecas_p1+=tabuleiro[0][i]
	if(pecas_p1>pecas_p2):
		return 1
	elif(pecas_p2>pecas_p1):
		return 2
	else:
		return 0

			


#vira o tabuleiro ps:recebe o tuplo
def vira_tabuleiro(estado):
	tabuleiro=estado[0].copy()
	t1=tabuleiro[len(tabuleiro)//2:]
	t2=tabuleiro[:len(tabuleiro)//2]
	p1=estado[2]
	p2=estado[1]
	return (t1+t2,p1,p2)

#verifica se o jogador pode jogar
def verifica_jogada(estado,jogada):
	if(jogada<0 or jogada>5 or estado[jogada]==1 or estado[jogada]==0):
		return False
	elif(tabuleiro_vazio(estado) and jogada+estado[jogada]<6):
		return False
	else:return True


#verifica se o tabuleiro do jogador adversario esta vazio
#recebe [x,x,x,x,x,x,x,x,x,X,X,X]
def tabuleiro_vazio(estado):
	for i in range(6,12):
		if(estado[i]>0):
			return False
		else:
			return True








if __name__ == "__main__":
    main()