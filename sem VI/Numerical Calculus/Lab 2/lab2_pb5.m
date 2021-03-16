x = [2, 4, 6, 8];
f = [4, 8, 14, 16];

[~, n] = size(x);
m = zeros(n, n+1);

m(:, 1) = x';
m(:, 2) = f';

for col = 3:n+1
    for line = 1:n
        if line + (col - 2) <= n && not(isnan(m(line+1, col-1)))
            m(line, col) = (m(line+1, col-1) - m(line, col-1)) / (m(line + col - 2, 1) - m(line, 1));
        else
            m(line, col) = nan;
        end
    end
end

display(m)