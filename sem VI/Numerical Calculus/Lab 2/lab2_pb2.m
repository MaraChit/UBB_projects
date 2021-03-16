% a.
T = @(n, t) cos(n * acos(t));
t = -1:0.01:1;
hold on;

title('Chebyshev polynomials')
plot(t, T(1, t), 'b');
plot(t, T(2, t), 'r');
plot(t, T(3, t), 'g');


% b.
n = 10;

for i = 1:n
  plot(t, Cheb(i, t));
end
