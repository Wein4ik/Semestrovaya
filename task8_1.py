def split_two_numbers(data_str):
    nums = data_str.split()
    return int(nums[0]), int(nums[1])


def get_plane(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4


input_1 = input()
input_2 = input()

x1, y1 = split_two_numbers(input_1)
x2, y2 = split_two_numbers(input_2)

if get_plane(x1, y1) == get_plane(x2, y2):
    print('Да')
else:
    print('Нет')
