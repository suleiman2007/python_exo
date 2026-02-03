date = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]
annee = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
input_annee = int(input())
if input_annee > 2011:
    while input_annee not in date:
        input_annee -= 12
elif input_annee < 2000:
    while input_annee not in date:
        input_annee += 12
print(annee[date.index(input_annee)])