x=0:0.001:10;f = (1+cos(pi*x))./(1+x);xx = linspace(0,10,21);f2 = (1+cos(pi*xx))./(1+xx);m = length(xx);P = zeros(1,m);N = length(x);L = zeros(1,N);for j = 1:N  s1 = 0;  s2 = 0;  for i = 1:m    P(i) = Ai_test(i,xx);  s1 = s1 + P(i)*f2(i)/(x(j)-xx(i));  s2 = s2 + P(i)/(x(j)-xx(i));endforL(j) = s1/s2;endhold onplot(x,f)plot(x, L, 'r')hold off