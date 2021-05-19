f = @(x) x .^ 3 - x .^ 2 - 1;
x0 = 1;
x1 = 2;
e = 10 ^(-4);
N=100;
i=1;
while i<N
  x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0));
  if abs(x-x1)<eps
    printf("Solution: %f \n",x);
    printf("Iterations: %d\n",i);
    return
  endif
  i = i+1;
  x0 = x1;
  x1=x;
 end