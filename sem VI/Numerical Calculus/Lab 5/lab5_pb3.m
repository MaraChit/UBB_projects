x = [-5:0.1:5];
f = @(x)sin(2 .* x);
fx = f(x);


%plot the function f
plot(x,fx,'*')
hold on;

%plot the Hermite interpolation
t = linspace(-5, 5, 15);
fd = @(x)2.*cos(2.*x);
fdt = fd(t);
ft = f(t);
rez = HermitePol(t, ft, fdt,x);
plot(x, rez, '-r')
hold on;
