square(X,I):-T is I*I, T<X, I2 is I+1, square(X,I2),!.
square(X,I):-T is I*I, T=X.

cmmmdc(A,B,_,X):-A=B,X=A.
cmmmdc(A,B,I,X):-A mod I =0,mod(B,I)=0,X=I.
cmmmdc(A,B,I,X):-I=<A, I=<B,I2 is I+1,cmmmdc(A,B,I2,X).

