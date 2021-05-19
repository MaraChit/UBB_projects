f = @(x) (x-2)^2 - log(x);
a = 1;
b = 2;
e = 10^(-4);
N = 100;
n = 0;

if f(a)*f(b)<0
  while n<=N
    n = n+1;
    c = (f(b)*a - f(a)*b)/(f(b)-f(a));
    if abs(f(c))<=e
      fprintf('Approx value with false position: %f\n', x);
      fprintf('Iterations: %d\n', n);
      return
    endif
    
    if f(a) * f(c)<0
      b = c;
    else
      a = c;
    endif
    
  endwhile
  fprintf('Exceeded number of iterations');
else
  fprintf('Exceeded number of iterations');
endif