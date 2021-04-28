A = [10 7 8 7; 7 5 6 5; 8 6 10 9; 7 5 9 10];
B = [32 23 33 31]';

%a
printf("a)\n"); 
printf("the result:\n");  
X = gauss(A,B)'
printf("k2 = %4.2e, k1 = %4.2e, kinf = %4.2e\n",cond(A,2),cond(A,1),cond(A,inf));

%b
printf("\nb)\n"); 
Bb = [32.1 22.9 33.1 30.9]';
printf("the result for B~=:\n");  
Xb = gauss(A,Bb)'

input_err = norm(B-Bb)/norm(B);
out_err = norm(X-Xb)/norm(X);
printf("input error: %d\n",input_err); 
printf("output error: %d\n",out_err); 
raport = out_err/input_err

%c
printf("\nc\n"); 
Aa = [10 7 8.1 7.2; 7.08 5.04 6 5; 8 5.98 9.89 9; 6.99 4.99 9 9.98];
printf("the result for A~=:\n");  
Xa = gauss(Aa,B)'

input_errA = norm(A-Aa)/norm(A);
out_errA = norm(X-Xa)/norm(X);
printf("input error: %d\n",input_errA); 
printf("output error: %d\n",out_errA); 
raportA = out_errA/input_errA
