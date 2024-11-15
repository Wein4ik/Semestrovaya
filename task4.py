spisok = int(input("Введите четырёхзначное число: "))
n = 1
new_per = 0
while spisok != 0:
    lust_number = spisok % 10 + 1
    if lust_number == 10:
        lust_number = 0
    new_per += lust_number * n
    spisok = spisok // 10
    n = n * 10

print(f"Новое число: {new_per}")
