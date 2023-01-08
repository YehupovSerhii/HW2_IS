# hw_14
# Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):

# Lecture  1: 17 Oct 2022 19:15
# Lecture  2: 20 Oct 2022 19:15
# ...
# Lecture  9: 14 Nov 2022 19:15
# Lecture 10: 17 Nov 2022 19:15
# ...
# Lecture 32: 02 Feb 2023 19:15


import datetime
print("Пример:")
print("Lecture 32: 02 Feb 2023 19:15")
print()
print("Результат:")

name="Lecture"
punct=":"
time="19:15"
d1 = datetime.date(2022, 10, 17)
count=0
i=0
while count<=31:
    dt = d1 + datetime.timedelta(i)
    k=int(dt.weekday())
    i+=1
    if k==0 or k==3:
        count+=1
        u=dt.strftime("%d %b %Y")
        print(f"{name:3}{count:>3}{punct}{u:>12}{time:>6}")

