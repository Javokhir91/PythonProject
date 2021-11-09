# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.

def thesaurus_adv(*args):
    list = dict()
    for name in args:
        index_1 = name.split()[1][0]
        index_2 = name[0]
        if index_1 not in list:
            list[index_1] = dict()
        if index_2 not in list[index_1]:
            list[index_1][index_2] = []
        list[index_1][index_2].append(name)
    return list



print(thesaurus_adv("Александр Владимиров", "Алексей Макаров",
                    "Владислав Харламов", "Тимофей Сергеев", ))