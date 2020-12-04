%p(vazio ou ocupado,linha,coluna)
p('vazio',_,_).
p('rainha',_,_).
resolve(N):-
    assert(tamanho(N)),
    cria_tabuleiro(N,Tabuleiro),
    %findall(Final,resolve(Tabuleiro,N,Final),L),
    resolve(Tabuleiro,N,Final),
    %sort(L,Sorted),
    print_tabuleiro([Final],N).
    %length(Sorted,N_solucoes),write(N_solucoes).

%recebe tabuleiro com n tamanho e da-o resolvido(Final)
resolve(Tabuleiro,N,Final):-resolve(Tabuleiro,N,[],Final).
resolve(X,0,_,X).
resolve([p('vazio',X,Y)|T1],N,Resto,[p('rainha',X,Y)|T2]):-
    \+ataca(p(_,X,Y),Resto),
    \+ataca(p(_,X,Y),T1),
    append([p('rainha',X,Y)],Resto,Resto1),
    N1 is N-1,
    resolve(T1,N1,Resto1,T2).

resolve([p('vazio',X,Y)|T1],N,Resto,[p('vazio',X,Y)|T2]):-
    append([p('vazio',X,Y)],Resto,Resto1),
    resolve(T1,N,Resto1,T2).



%true se p('rainha',X,Y)ataca alguma outra rainha
ataca(Posicao,Tabuleiro):-
    (ataca_linha(Posicao,Tabuleiro);
    ataca_coluna(Posicao,Tabuleiro);
    ataca_diagonal(Posicao,Tabuleiro)).
ataca_linha(p(_,X,_),Tabuleiro):-
    member(p('rainha',X,_),Tabuleiro).
ataca_coluna(p(_,_,Y),Tabuleiro):-
    member(p('rainha',_,Y),Tabuleiro).
ataca_diagonal(Posicao,Tabuleiro):-
    tamanho(N2),
    delete(Tabuleiro,Posicao,Tabuleiro1),
    (cima_direita(Posicao,Tabuleiro1,N2);
    cima_esquerda(Posicao,Tabuleiro1,N2);
    baixo_direita(Posicao,Tabuleiro1,N2);
    baixo_esquerda(Posicao,Tabuleiro1,N2)).

cima_direita(p(_,X,Y),List,N):-
    X1 is X-1,
    Y1 is Y+1,
    limite(X1,Y1,N),
    ((member(p('rainha',X1,Y1),List),!);
    cima_direita(p(_,X1,Y1),List,N)).

cima_esquerda(p(_,X,Y),List,N):-
    X1 is X-1,
    Y1 is Y-1,
    limite(X1,Y1,N),
    (member(p('rainha',X1,Y1),List);
    cima_esquerda(p(_,X1,Y1),List,N)).

baixo_direita(p(_,X,Y),List,N):-
    X1 is X+1,
    Y1 is Y+1,
    limite(X1,Y1,N),
    (member(p('rainha',X1,Y1),List);
    baixo_direita(p(_,X1,Y1),List,N)).
baixo_esquerda(p(_,X,Y),List,N):-
    X1 is X+1,
    Y1 is Y-1,
    limite(X1,Y1,N),
    (member(p('rainha',X1,Y1),List);
   baixo_esquerda(p(_,X1,Y1),List,N)).



cria_tabuleiro(N,Tabuleiro):-
    findall(p('vazio',X,Y),(numlist(1,N,L),member(X,L),member(Y,L)),Tabuleiro).

limite(X,Y,N1):-N is N1,X=<N,X>0,Y>0,Y=<N.

print_tabuleiro([],_).
print_tabuleiro([H|T],N):-
    %write(H),nl,
    print_tabuleiro(H,N,1),
    nl,
    print_tabuleiro(T,N).
print_tabuleiro([],_,_).
print_tabuleiro([p('rainha',_,_)|T],N,Nr1):-
    write('r'),
    (   Nr1==N->nl,Nr2 is 1;write(' '),Nr2 is Nr1+1),
    print_tabuleiro(T,N,Nr2).
print_tabuleiro([p('vazio',_,_)|T],N,Nr1):-
    write('v'),
    (   Nr1==N->nl,Nr2 is 1;write(' '),Nr2 is Nr1+1),
    print_tabuleiro(T,N,Nr2).

