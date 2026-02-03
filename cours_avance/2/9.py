n = int(input())
cnt_I = 0
cnt_II = 0
cnt_III = 0
cnt_IV = 0
for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt_I += 1
    elif x < 0 and y > 0:
        cnt_II += 1
    elif x < 0 and y < 0:
        cnt_III += 1
    elif x > 0 and y > 0:
        cnt_IV += 1
print('Первая четверть:', cnt_I)
print('Вторая четверть:', cnt_II) 
print('Третья четверть:', cnt_III) 
print('Четвертая четверть:', cnt_IV)
    