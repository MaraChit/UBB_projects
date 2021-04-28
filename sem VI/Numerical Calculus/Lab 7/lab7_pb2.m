t = [0 10 20 30 40 60 80 100];
p = [0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];
exactValue = 0.095848;

%a

% 2nd degree polynomial 
P2 = polyfit(t,p,2);
fprintf('phi(x)=%f x^2 + %f x + %f\n',P2);
res1 = polyval(P2,45)
E1 = exactValue - res1

% 3rd degree polynomial
P3 = polyfit(t,p,3);
fprintf('phi(x)=%f x^3 + %f x^2 + %f x + %f\n',P3);
res2 = polyval(P3,45)
E2 = exactValue - res2


%b
xp = 0:0.1:100;
hold on
%plot the points
plot(t,p,'bo')
%plot the 2nd degree polynomial
plot(xp,polyval(P2,xp),'r-');
%plot the 3rd degree polynomial
plot(xp,polyval(P3,xp),'g-');
legend('points','2nd degree polynomial','3rd degree polynomial');