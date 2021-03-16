x = -1:0.01:3;

hold on;

for i = 0:6
  plot(x, Taylor(i, x));
end

title('First 6 Taylor polynomials');