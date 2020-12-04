%p(vazio ou ocupado,linha,coluna)
p('vazio',_,_).
p('rainha',_,_).
%verifica se a posicao ataca alguma rainha
teste(N):-
    cria_tabuleiro(N,Tabuleiro),
    get_linha(Tabuleiro,2,Linha),
    write(Linha),nl,
    get_coluna(Tabuleiro,2,Coluna),
    write(Coluna).
ataca(p(_,X,Y),Tabuleiro):-
    get_linha().
cria_tabuleiro(N,Tabuleiro):-cria_tabuleiro(N,0,Tabuleiro),!.
cria_tabuleiro(N,N,[]).
cria_tabuleiro(N,Nr1,[H|T]):-
    cria_linha(N,H,Nr1),
    Nr2 is Nr1+1,
    cria_tabuleiro(N,Nr2,T).

cria_linha(N,H,Linha):-cria_linha(N,0,H,Linha).
cria_linha(N,N,[],_).
cria_linha(N,Nr1,[p(_,Linha,Nr1)|T],Linha):-
    Nr2 is Nr1+1,
    cria_linha(N,Nr2,T,Linha).

get_linha(Tabuleiro,N,Linha):-get_linha(Tabuleiro,N,0,Linha).
get_linha([Linha|_],N,N,Linha):-!.
get_linha([Linha],N,N,Linha):-!.
get_linha([_|T],N,Nr1,Linha):-
    Nr2 is Nr1+1,
    get_linha(T,N,Nr2,Linha).

get_coluna([],_,[]).
get_coluna([H|T], I, [R|X]):-
   get_linha(H, I, R),
get_coluna(T,I,X).

get_diagonal
