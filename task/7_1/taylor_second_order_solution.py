a, b, x = map(float, input().split())
grad = 2.0 * a * x + b
hess = 2.0 * a
x_new = x - grad / hess
print('{:.6f}'.format(x_new))
