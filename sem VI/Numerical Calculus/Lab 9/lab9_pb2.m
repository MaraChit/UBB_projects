f = @(x) 2./(1 + x.^2);
a = 0;
b  = 1;
eps = 10^(-4);

q0 = (1 / 2) * (f(a) + f(b));
fprintf("Romberg(7): %.6f\n", romberg(f, q0, 1, a, b, eps));
