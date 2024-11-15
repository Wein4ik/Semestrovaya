def edenitsi(n):
    if n == 0:
        return ""
    if n == 1:
        return "один"
    if n == 2:
        return "два"
    if n == 3:
        return "три"
    if n == 4:
        return "четыре"
    if n == 5:
        return "пять"
    if n == 6:
        return "шесть"
    if n == 7:
        return "семь"
    if n == 8:
        return "восемь"
    if n == 9:
        return "девять"


def deciatki(n):
    if n == 2:
        return "Двадцать"
    if n == 3:
        return "Тридцать"
    if n == 4:
        return "Сорок"
    if n == 5:
        return "Пятьдесят"
    if n == 6:
        return "Шестьдесят"
    if n == 7:
        return "Семьдесят"
    if n == 8:
        return "Восемьдесят"
    if n == 9:
        return "Девяносто"


n = int(input("Введите число: "))
if 20 <= n <= 99:
    b = edenitsi(n % 10)
    d = deciatki(n // 10)
    print(f"{d} {b}")
else:
    print('Некорректный ввод. Число должно быть от 20 до 99 включительно.')
