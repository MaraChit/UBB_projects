a=0; b=1;
f = @(x) 2./(1+x.^2);

format long
Int = integral(f,a,b) 
Int_trapez = (b-a)/2*(f(a)+f(b)) 
Int_simpsons = (b-a)/6*(f(a)+4*f((b-a)/2) + f(b))

 
 
%b)
%the function
fplot(f,[a,b]);
hold on
%the trapezium with the vertices (0; 0);(0; f(0));(1; f(1)) and (1; 0):
fill([0,0,1,1],[0,f(0),f(1),0],'b');