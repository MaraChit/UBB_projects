a = 0; b = pi;
f = @(x) 1 ./ (4+sin(20 .*x));
n1 = 10; n2 = 30;

r1 = simpson(f, a, b, n1);
r2 = simpson(f, a, b, n2);

printf("For n=%d, approximation of f is %d\n", n1, r1);
printf("For n=%d, approximation of f is %d\n", n2, r2);