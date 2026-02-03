s1, s2, s3 = set(map(int, input())), set(map(int, input())), set(map(int, input()))
print(s1 & s2 | s2 & s3 | s1 & s3)