function z = gauss(A,b, N, eps) 
  [m,n]=size(A);
  xJ_old=zeros(m,1);
  xJ_new=xJ_old;
  nr_it=0;

  fprintf('Using Gauss:\n')

  while nr_it<=N
    
    for i=1:m
        aux_suma1 = A(i,i+1:n)*xJ_old(i+1:n,:);
        aux_suma2 = A(i,1:i-1)*xJ_new(1:i-1,:);
        xJ_new(i) = 1/A(i,i)*(b(i)- aux_suma1 - aux_suma2); 
    end
    
    if abs(xJ_new-xJ_old)<eps
      fprintf('Solutia este:\n')
      disp(xJ_new)
      fprintf('Numarul de iteratii:%d\n',nr_it)
      fprintf('\n\n')
      z=xJ_new;
      return
    end
   
    xJ_old=xJ_new;
    nr_it=nr_it+1;
  end
  disp('Numarul de iteratii a fost depasit')
endfunction