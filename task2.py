def split_two_numbers(data_str):
    nums = data_str.split()
    return int(nums[0]), int(nums[1])


def summa(chislo):
    n = 0
    while chislo != 0:
        n += chislo % 10
        chislo = chislo // 10
    return n


input_1 = input()

n = 0
perchis, vtorchis = split_two_numbers(input_1)
c = summa(perchis)
b = summa(vtorchis)
print(b * c)
