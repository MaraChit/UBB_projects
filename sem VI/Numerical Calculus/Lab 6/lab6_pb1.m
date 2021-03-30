%a)
X = [0 pi/2 pi 3.*pi/2 2.*pi];
x = 0:0.001:2*pi;
f = @(x) sin(x);
fx = f(x);

fct = f(pi/4)
sp = spline(X, f(X), pi/4)
cl = spline(X, [1 f(X) 1], pi/4)



%b)
s = spline (X, f(X), x);
cs = spline (X, [1 f(X) 1], x);

plot(x, s, 'b')
hold on
plot(x, cs, 'g')
hold on
plot(X, f(X), 'o')
