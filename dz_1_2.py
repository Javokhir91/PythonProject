cube_list = []
for a in range(1, 1000, 2):
    cube_list.append(a ** 3)

result = 0
for a in range(len(cube_list)):
    sum_cubs = 0
    list_cubs = cube_list[a]
    while list_cubs > 0:
        sum_cubs += list_cubs % 10
        list_cubs = list_cubs // 10
    if sum_cubs % 7 == 0:
        result += (cube_list[a])
print(f'сумма чисел из списка: {result}')

result = 0
for a in range(len(cube_list)):
    cube_list[a] += 17
    sum_cubs = 0
    list_cubs = cube_list[a]
    while list_cubs > 0:
        sum_cubs += list_cubs % 10
        list_cubs = list_cubs // 10
    if sum_cubs % 7 == 0:
        result += (cube_list[a])
print(f'сумма чисел увеличенных на 17{result}')