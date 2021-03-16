i = 0:6;
h = 0.25;
x = 1 + i .* h;
f = sqrt(5 .* (x .^ 2) + 1);
[~, n] = size(x);
m = zeros(n, n+1);
  
m(:, 1) = x';
m(:, 2) = f';

for col = 3:n+1
    for line = 1:n
        if line + 1 <= n && not(isnan(m(line+1, col-1)))
            m(line, col) = m(line+1, col-1) - m(line, col-1);
        else
            m(line, col) = nan;
        end
    end
end
  
display(m)