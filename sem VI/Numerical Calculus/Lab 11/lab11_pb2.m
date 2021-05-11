A=[3,1,1;-2,4,0;-1,2,-6];

b=[12;2;-5];

eps=10^(-5);
N=100;
x=A\b

jac = jacobi(A,b, N, eps);
gss = gauss(A,b,N,eps);
rlx = relaxation(A,b,N,eps);