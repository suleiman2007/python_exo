n = int(input())
lst_input = [list(map(int, input().split())) for i in range(n)]
lst = []

for i in range(n):
    lst.extend((lst_input[i])[:i+1])
    

print(max(lst))