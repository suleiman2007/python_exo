masse, rost = float(input()), float(input())
if 18.5 <= masse / (rost * rost) <= 25:
    print('Оптимальная масса')
elif 25 < masse / (rost * rost):
    print('Избыточная масса')
else:
    print('Недостаточная масса')