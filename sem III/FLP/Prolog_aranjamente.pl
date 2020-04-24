comb([H|_], 1, [H]).
comb([_|T],K,R):-comb(T,K,R).
comb([H|T],K,R):-K>1,K2 is  K-1, comb(T,K2,R2), R =[H|R2].
main(L,N,R):- findall(Rez,comb(L,N,Rez),R).

findd([El|_],El).
findd([_|T],El):- findd(T,El).

del([],_,[]).
del([El|T],El,R):- R=T.
del([H|T],El,R):-H\=El,del(T,El,R2),R=[H|R2].


perm([],[]).
perm(L,[E|R]):-findd(L,E),del(L,E,RR),perm(RR,R).

aranj(L,K,R):-comb(L,K,RR),perm(RR,R).
