def check_triangle(n_1, n_2, n_3):
    b = [n_1, n_2, n_3]

    # проверяем что ни одна из сторон треугольника не равна 0
    for i in range(len(b)):
        if b[i] <= 0:
            return 0

    # проверяем условие существования треугольника
    if n_1 + n_2 <= n_3 or n_1 + n_3 <= n_2 or n_2 + n_3 <= n_1:
        return 0

    # проверяем равносторонний ли треугольник
    if n_1 == n_2 == n_3:
        return 3

    # проверяем что треугольник неравнобедренный
    if n_1 != n_2 != n_3:
        return 1

    # если достигли этой строчки, это означает что треугольник равнобедренный
    return 2


a = int(input())
b = int(input())
c = int(input())

result = check_triangle(a, b, c)
print(result)
