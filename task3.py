def chislo(n):
    chis = 0
    step = 0
    while n > 0:
        last_number = n % 10 // 2
        chis = last_number * (10 ** step) + chis
        n //= 10
        step += 1
    return chis


n = int(input("Введите число: "))
a = chislo(n)
print(a)
