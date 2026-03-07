# FULL PYTHON SOLUTION
f1, f2 = map(float, input().split())
trend = 'inc' if f1 > 0 else ('dec' if f1 < 0 else 'flat')
shape = 'convex' if f2 > 0 else ('concave' if f2 < 0 else 'linear')
print(trend + ' ' + shape)
