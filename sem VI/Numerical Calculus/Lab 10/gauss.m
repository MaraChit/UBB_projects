function z = gauss(matrix, b)
  
  n = length(matrix);
  
  s = [];
  p = [];
  x = []; % vector of solution
  for i = 1:4
    x(end+1) = 0;
  endfor
  
  %compute the array of row max elems
  for i=1:n
    stemp = 0;
    for j = 1:n
      stemp = max(stemp, abs(matrix(i,j)));
    endfor
    s(end+1) = stemp;
    p(end+1) = i;
  endfor
  
  %find largest scaled column entry
  for k =1:n-1
    rmax = 0;
    for i = k:n
      r = abs(matrix(p(i),k)/s(p(i)));
      
      if (r > rmax)
        rmax = r;
        j = i  ;
      endif
    endfor
    
    %change row pointers
    temp = p(k);
    p(k) = p(j);
    p(j) = temp;
    
    %elimination on submatrix
    for i = k+1:n
      matrix(p(i),k) = matrix(p(i),k)/matrix(p(k),k);
      for j = k+1:n
        matrix(p(i), j) = matrix(p(i),j) - matrix(p(i),k)*matrix(p(k),j);
      endfor
    endfor
  endfor
  
  %forward elimination
  for k = 1:n-1
    for i = k+1:n
      b(p(i)) = b(p(i)) - matrix(p(i),k)*b(p(k));
    endfor
  endfor
  
  %backward solve
  for i = n:-1:1
    s = b(p(i));
    for j = i+1:n
      s = s - matrix(p(i),j)*x(j);
    endfor
    x(i) = s / matrix(p(i), i);
  endfor
  
  z = x;
  
endfunction