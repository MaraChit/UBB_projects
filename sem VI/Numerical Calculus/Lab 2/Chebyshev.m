function ret = Cheb(n, x)
  if (n == 0)
    ret = 1;
  elseif(n == 1)
    ret = x;
  else
    ret = 2 * x .* Cheb(n - 1, x) - Cheb(n - 2, x);
  end
end