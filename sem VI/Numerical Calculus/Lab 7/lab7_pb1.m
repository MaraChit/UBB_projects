x = 1:7;
f  = [13, 15, 20, 14, 15, 13, 10];

% method 1
A = [sum(x.^2),sum(x);sum(x),length(x)];
B = [sum(x.*f);sum(f)];

X = linsolve(A,B); % X = B*A^(-1) 
fprintf('phi(x)=%f x + %f\n',X);
v1 = polyval(X,8) %V = X(1)*8 + X(2)

%method 2
P = polyfit(x,f,1);
fprintf('phi(x)=%f x + %f\n',P);
V2 = polyval(P,8)

%plot the points
plot(x,f,'bo');
hold on

%plot the polynomial
xp = 1:0.01:8;
plot(xp, polyval(P,xp), 'r-');