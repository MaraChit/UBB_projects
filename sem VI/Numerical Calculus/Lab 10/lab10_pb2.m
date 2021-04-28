nmin = 10;
nmax = 15;
n = [nmin:nmax];

for i =1:length(n)
    H = hilb(n(i));
    
    %k2 = norm(H,2) * norm(inv(H),2)
    k2 = cond(H,2);  
    k1 = cond(H,1);
    kinf = cond(H,inf);
    %disp(H);
    
    printf("n = %d\n", n(i));
    printf("k2 = %4.2e, k1 = %4.2e, kinf = %4.2e\n",k2,k1,kinf);
endfor