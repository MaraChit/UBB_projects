%approximate sqrt(115) with precision 1/(10^3)
x = [81 121 100 144];
f = @(x) sqrt(x);

rez = AitkenPol_stud(x,f(x),115)