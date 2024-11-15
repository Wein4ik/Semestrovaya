def sred_znach(n):
    k = 0
    for i in range(len(n)):
        k += n[i]
    k = k / len(n)
    return k
def okrug(n):
    if n < 2.5:
        return 2
    if n >= 2.5 and n < 3.5:
        return 3
    if n >= 3.5 and n < 4.5:
        return 4
    if n >= 4.5:
        return 5
spisok = []
n = int(input(""))
for i in range(6):
    spisok.append(n % 10)
    n //= 10

a = sred_znach(spisok)
a = round(a,1)

qwerty = okrug(a)

print(f"Ваш средний балл: {a}. Ваша оценка за четверть: {qwerty}")
