n,m,k,x,y,z = (int(input()) for i in range(6))
total = (n - x) + (m - x - y) + (k - y) + x + y + z
print(total)