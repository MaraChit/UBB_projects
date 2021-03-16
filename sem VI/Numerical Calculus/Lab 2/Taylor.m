function ret = Taylor(n, x)
  if (n == 0)
    ret = 1;
  else
    ret = Taylor(n - 1, x) + x .^ n * exp(0)  / factorial(n);
  end
end