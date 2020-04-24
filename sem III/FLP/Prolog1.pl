%Pb8 a)Write a predicate to determine if a list has even numbers of
% elements without counting the elements from the list.
%)EvenNrElems(l1 l2 ... ln) = false, l has 1 elem
%                              true, l is empty
%                              EvenNrElems(l3 ... ln),otherwise
%
%
%
%EvenNrElems(L: list, M int)
%flow model (i, o)
evenNrElems([],true).
evenNrElems([_|[]],false).
evenNrElems([_|T],R):- [_|B] = T ,evenNrElems(B,R).


%b) Write a predicate to delete first occurrence of the minimum number from a list.
% min(l1...ln,el)= el, l is empyy
%                  min(l2....ln,l1), l1<el
%                  min(l2...ln,el),otherwise
%min(L:list, E int, R int)
%flow model(i,i,o)
min([],R,R).
min([H|T],E,R):-H<E,!,min(T,H,R).
min([_|T],E,R):-min(T,E,R).


%remove(l1...ln,el) = 0, list is empty
%                     (l2....ln),el=l1
%                     l1U remove(l2....ln), otherwise
%remove(L:list, E int, R: list)
%flow model (i,i,o)
remove([],_,[]).
remove([H|T],E,R):-H=E,!,R=T.
remove([H|T],E,R):-remove(T,E,R1),R=[H|R1].

%removeFirst(L: list, R: list)
%flow model (i,o)
removeFirst([],[]).
removeFirst(H,R):- min(H,999,R2),remove(H,R2,R).
