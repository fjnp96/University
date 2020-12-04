
use_module(library(write)).
use_module(library(clpfd)).
%nonograma(Linhas,Colunas). true se for um nonograma
puzzle([H,T]):-nonograma(H,T).
nonograma(ConsL,ConsC):-
	length(ConsL,NC),
	length(ConsC,NL),
	matrix(Linhas,Colunas,NL,NC),
	%casos_unitarios(ConsL,Linhas,NL,NC),
	casos_possiveis(ConsL,NL,NC,CPLinhas),
	casos_possiveis(ConsC,NC,NL,CPColunas),
	resolve(Linhas,CPLinhas),
	resolve(Colunas,CPColunas),
	print_solucao(Linhas),!.
	
%trata das constraints unitarias
%casos_unitarios(ConsL,Linhas,NL,NC).
%casos_unitarios([],_,_,_).
%casos_unitarios([H1|T1],[H2|T2],NL,NC):-
%	(lenght(H1,1)->
%	caso_unitario(H1,T2,NL,NC),casos_unitarios(T1,T1,NL,NC));
%	casos_unitarios(T1,T1,NL,NC).

%caso_unitario().
%caso_unitario([H1|T1],[H2|T2],NL,NC):-
	
		
	
%resolve().
resolve([],_).
resolve([H1|T1],[H3|T3]):-
	member(H1,H3),
	resolve(T1,T3).
	
%resolve([HL|TL],[HC,HL],[H1|H2],)
%casos_possiveis(ConsL,N,CPLinhas)
casos_possiveis([],0,_,_).
casos_possiveis([H|T],NL,NC,CPLinhas):-
	length(CPLinhas,NL),
	NL1 is NL-1, 
	casos_possiveis(T,NL1,NC,Casos2),
	findall(Linha,list_exe(H,Linha,NC),Casos),
	append(Casos2,[Casos],CPLinhas).
	
%gera uma matrix com NL*NC tamanho
matrix(Linhas,Colunas,NL,NC):-
	length(Linhas,NL),
	length(Colunas,NC),
	transposta(Linhas,Colunas).



transposta([], []).
transposta([F|Fs], Ts) :-
    transposta(F, [F|Fs], Ts).

transposta([], _, []).
transposta([_|Rs], Ms, [Ts|Tss]) :-
        lists_firsts_rests(Ms, Ts, Ms1),
        transposta(Rs, Ms1, Tss).

lists_firsts_rests([], [], []).
lists_firsts_rests([[F|Os]|Rest], [F|Fs], [Os|Oss]) :-
        lists_firsts_rests(Rest, Fs, Oss).		
	
%Lista é uma linha com N tamanho com 0s ou 1s
line([],0).
line([H|T],X):-
	length([H|T],X),
	line(T,X1),
	X is X1+1,
	(H=0;
	H=1).

%List2 com tamanho N é uma possivel solucao para List1
%list_exe(List1,List2,N).
%List2 e a linha e List1 e a constraint

list_exe([],[],0).
list_exe(List1,List2,N):-
	line(List2,N),
	soma_lista(List1,X),
	count(List2,X),
	teste(List1,List2).
		
teste([],[]).
teste([H1|T1],Linha):-
	T1 \= [],
	tirar_zeros(Linha,Linha2),
	teste2(H1,Linha2,Linha3),
	verifica_espaco(Linha3,Linha4),
	teste(T1,Linha4).

teste([H1|[]],Linha):-
	tirar_zeros(Linha,Linha2),
	teste2(H1,Linha2,Linha3),
	tirar_zeros(Linha3,Linha4),
	teste([],Linha4).
	
tirar_zeros(Linha,Linha).
tirar_zeros([0|T],Linha):-
	tirar_zeros(T,Linha).
%recebe um numero(X) da lista, e diz se a list tem X 1s seguidos

teste2(0,Linha,Linha).
teste2(X,[1|T],Linha):-
	X>0,
	X1 is X-1,
	teste2(X1,T,Linha).

%verifica_espaco(Linha1,Linha2) 
%retorna True se Linha2 é a Linha1 com menos um espaco
verifica_espaco([0|Linha],Linha).  

%soma os valores da lista
soma_lista([],0).
soma_lista(A,B):-soma_lista(A,B,0).
soma_lista([],A,A).
soma_lista([A|A1],B,C):- C1 is A+C, soma_lista(A1,B,C1).	

%conta os nr pintados de uma linha
%count(List,N).

count(List,X):-
	soma_lista(List,X).	

%print_solucao
print_solucao([]).
print_solucao([H|T]):-
	print_solucao(T),
	write("\n"),
	print_solucao2(H).

print_solucao2([]).
print_solucao2([H|T]):-
	H is 1->(write("X"),print_solucao2(T));
	write(" "),
	print_solucao2(T).

%?-puzzle([[[1,1], [2,1,2],[2,1,1,2],[5,1,1,5],[4,1,1,5],[3,2,4],[3,4,4],[11],[4],[3,4,3],[10],[6,2],[11],[2,6],[10],[2,4,2],[4],[2,2],[8],[2,1,1,2],[2,2,2,2],[4,4],[8]],[[2],[5,1,1], [7,1,2,1,1],[5,2,1,2,3],[3,2,1,1,1,2,2],[1,5,2,3],[2,17],[12,1,1],[12,1,1],[2,17],[1,5,2,3],[2,1,1,1,2,2],[6,2,1,2,3],[5,1,1,1,1],[7,1,1],[5],[2]]]).

?-puzzle([[[1],[3],[1,1,1],[1],[1]],[[1],[1],[5],[1],[1]]]).
%exemplos da net
%?-puzzle([[[2,2],[7],[2,4],[7],[5],[3],[1]],[[3],[5],[2,3],[6],[6],[5],[3]]]).
%?-puzzle([[[3,5],[1,5],[1,6],[5],[2,4,1],[2,1],[3],[5,1],[1],[2,1,1]],[[1,4,1],[3,4,1],[1,3],[1,1],[3,1],[5],[5,1],[4,1,1],[5,1],[3]]]).
