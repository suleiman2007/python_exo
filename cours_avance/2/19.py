lst_input = [i for i in input().split()]
cnt = 0
lst_cnt = []
for i in lst_input:
    if i not in lst_cnt:
        lst_cnt.append(i)
        cnt += 1
print(cnt)