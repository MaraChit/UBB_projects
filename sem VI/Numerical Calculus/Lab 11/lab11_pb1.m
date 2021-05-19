A=[3, -1, 0, 0, 0, 0; -1, 3, -1, 0, 0, 0; 0, -1, 3, -1, 0, 0; 0, 0, -1, 3, -1, 0;
   0, 0, 0, -1, 3, -1; 0, 0, 0, 0, -1, 3];

b=[2; 1; 1; 1; 1; 2];

eps=10^(-3);
N=100;

x=A\b

jac = jacobi(A,b, N, eps);
gss = gauss(A,b,N,eps);
rlx = relaxation(A,b,N,eps);