r = rectangle('position',[0,0,3,5]);
[x,y] = ginput(10);

P = polyfit(x,y,2);
fprintf('phi(x)=%f x^2 + %f x + %f\n',P);

xp = 0:0.1:3;
hold on
%plot the points
plot(x,y,'bo');
%plot the 2nd degree polynomial
plot(xp,polyval(P,xp),'g-');
