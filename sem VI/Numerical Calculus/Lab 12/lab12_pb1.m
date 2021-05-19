f = @(x) x - cos(x);
fderiv = @(x) 1 + sin(x);
x0 = pi/4;
eps = 10 ^ (-4);
N = 100;
i = 1;

while i<N
  x = x0 - f(x0) / fderiv(x0);
  if abs(x - x0) < eps
    printf("Solution: %f \n",x);
    printf("Iterations: %d\n",i);
    return
  endif
  i = i + 1;
  x0 = x;
 end