%X é o nonograma resolvido

puzzle([Linhas,Colunas]):-
    len(Linhas,Colunas,Length),
    nonograma(Linhas,Colunas,X,Length).
len(A,B,Length):-length(A,Length), length(B,Length).
nonograma([],[],_,_).
nonograma([L|L1],[C|C1],X,Var):-
    soma_lista(L,Lsomado),
    soma_lista(C,Csomado),
    conta_cores(X,Var,Lsomado,"linha"),
    conta_cores(X,Var,Csomado,"coluna"),
    Var1 is Var+1,
    nonograma(L1,C1,X,Var1).


% nonograma([[1],[3],[1,1,1],[1],[1]],[[1],[1],[5],[1],[1]],[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[0,0,1,0,0],[0,0,1,0,0]],_).
%

%soma a lista
soma_lista([],0).
soma_lista(A,B):-soma_lista(A,B,0).
soma_lista([],A,A).
soma_lista([A|A1],B,C):- C1 is A+C, soma_lista(A1,B,C1).

%conta cores de uma lista ou seja os 1's
% Nano é a matriz do desenho, Nr_linha/coluna é a linha, X é o nr total
% de 1's conta_cores(Matriz,nr_linha,valor,'linha'ou'coluna').
conta_cores([],_,0,_).
conta_cores(Nano,Nr,X,Y):-
    Y="linha" -> conta_cores(Linha,X),
    get_linha(Nano,Nr,Linha);
    Y="coluna"->conta_cores(Coluna,X),
    get_coluna(Nano,Nr,Coluna).
conta_cores(Lista,X):-conta_cores2(Lista,X,0).
conta_cores2([],A,A).
conta_cores2([A|A1],B,C):-
   (A is 0->conta_cores2(A1,B,C));
    (A is 1->C1 is A+C,conta_cores2(A1,B,C1)).
%get_linha(matriz,nr_linha,linha).
%nr_linha/coluna começa em 0
%
get_linha([Linha],0,Linha).
get_linha([Linha|_],0,Linha).
get_linha([_|T],X,A):-
    X1 is X-1,
    get_linha(T,X1,A).

get_coluna([],_,[]).
get_coluna([H|T],X,[Value|Lista]):-
    get_coluna(T,X,Lista),
    get_value(H,X,Value).
%vai buscar a cor á matriz e adiciona a uma lista
get_value([Value],0,Value).
get_value([Value|_],0,Value).
get_value([_|Lista],X,Value):-
    X1 is X-1,
    get_value(Lista,X1,Value).

