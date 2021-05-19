f = @(E) E - 0.8 * sin(E) - 2 * pi / 10;
fderiv = @(E) 1 - 0.8 .* cos(E);
E0 = 1;
N = 6;
i = 1;
while i<=N
  E = E0 - f(E0)/fderiv(E0);
  printf("%d. Solution = %f \n",i,E);
  i = i+1;
  E0 = E;
 end