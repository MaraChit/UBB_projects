%1. Write a predicate to generate the list of all subsets with all
% elements of a given list. Eg: [2, 3, 4] N=2 => [[2,3],[2,4],[3,4]]
%
%
%
%
%lengthList(l1...ln):0, list is empty
%                     1+lengthList(l2...ln)
%flow model (i,o)
%lengthList(L: list, Len: int)

lengthList([],0).
lengthList([_|T],Len):- lengthList(T,Len2), Len is Len2+1.

%nrOccurences(l1...ln,e):0, list is empty
%                       :1+nrOccurences(l2...ln,e), if e=l1
%                       :nrOccurences(l2...ln,e), otherwise
%flow model (i,i,o)
%nrOccurences(L:list, El: int, X: int)

nrOccurences([],_,0).
nrOccurences([H|T],El,X):- H=:=El,nrOccurences(T,El,X2),X is X2+1.
nrOccurences([H|T],El,X):- H=\=El, nrOccurences(T,El,X).

%checkSet(l1..ln):true, list is empty
%                :checkSet(l2...ln) if nrOccurences(l2...ln,l1)=0
%                :false, otherwise
%flow model(i)
%checkSet(L:list)

checkSet([]).
checkSet([H|T]):-nrOccurences(T,H,0),checkSet(T).

%generateSets(l1..ln):[], list is empty
%                    :l1 U generateSets(l2...ln)
%                    :generateSets(l2...ln)
%flow model(i,o).
%generateSets(L: list, R: list).
generateSets([],[]).
generateSets([H|T],[H|T2]):-generateSets(T,T2).
generateSets([_|T],T2):-generateSets(T,T2).

%flow model(i,i,o)
%main(L:list, N: int, Aux:list)

main(L,N,Aux):- generateSets(L,Aux),lengthList(Aux,N),checkSet(Aux).

%flow model (i,i,o)
%theRealMain(L:list,N:int,R:list)

theRealMain(L,N,R):- findall(Aux, main(L,N,Aux), R).

%example: theRealMain([2,5,7,4],3,R).
%         theRealMain([1,2,3,1,4,5],2,R).
