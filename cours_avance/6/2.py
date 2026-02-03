n,m,k,x,y,z,t,a = (int(input()) for i in range(8))
q = (n + m - x - t)
s = (m + k - y - t)
d = (n + k - z - t)
book_1 = (n - q - d - t) + (m - q - s - t) + (k - s - d - t)
book_2 = q + s + d
book_0 = a - (book_1 + book_2 + t)
print(book_1, book_2, book_0, sep='\n')