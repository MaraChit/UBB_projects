%2.
% a. Sort a list with keeping double values in resulted list.
% E.g.: [4 2 6 2 3 4] --> [2 2 3 4 4 6]

%a)max(l1....ln, max) = max, list is empty
%                       max(l2...ln,l1),l1>max
%                       max(l2...ln,max),otherwise
%max(L:list,M: int,R: int);
%flow model (i,i,o).

max([],R,R).
max([H|T],M,R):-H>M,!,max(T,H,R).
max([_|T],M,R):-max(T,M,R).

%remove(l1....ln, el) = 0 , list is empty
%                       (l2...ln),l1=el
%                       l1U remove(l2...ln), otherwise
%remove(L:list,E: int,R:list);
%flow model(i,i,o).

remove([],_,[]).
remove([H|T],E,R):-H=E,!,R=T.
remove([H|T],E,R):-remove(T,E,R1),R=[H|R1].


%main(L :list,A: list, R: list)
%flow model (i,o,o)

main([],A,A).
main(L,R,K):- max(L,0,M),remove(L,M,T),R1=[M|R],main(T,R1,K2),K2=K.


% b. For a heterogeneous list, formed from integer numbers and list of
% numbers, write a predicate to sort every
%sublist, keeping the doubles.
%Eg.: [1, 2, [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
%[1, 2, [1, 4, 4], 3, 6, [1, 3, 7, 9, 10], 5, [1, 1, 1], 7].

%sortSublist(l1....ln): 0 if list is empty
%                     : main(l1,[],[])UsortSublist(l2...ln), l1-list
%                     :l1U sortSublist(l2...ln)
%sortSublist(L: list, R:list)
%flow model (i,o)

sortSublist([],[]).
sortSublist([H|T],R):-is_list(H),!,main(H,[],K),sortSublist(T,R1),R=[K|R1].
sortSublist([H|T],R):-sortSublist(T,R1),R=[H|R1].


