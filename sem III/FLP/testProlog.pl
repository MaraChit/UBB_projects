%replaceOdd(l1...ln):0 if list is empty
%                   :0 U replaceOdd(l3....ln)
%replaceOdd(L:list,A: List,X:list)
%flow model(i,i,o)


replaceOdd([],[]).
replaceOdd([_|T],R):- T=[_|B],write(T),write(B), replaceOdd(B,R1), R1=[0|R].

%factorial(x,r,i):r, x=i
%                :factorial(x,r*i,i+1),i<x
%
%factorial(X: int, I: int,P: int R:int)
%flowmodel(i,i,i,o)
%
factorial(X,I,P,R):- X=I, R is P*X.
factorial(X,I,P,R):-I<X,P2 is I*P, I2 is I+1, factorial(X,I2,P2,R2),R=R2.



