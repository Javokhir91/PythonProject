tutors = ['Кристина', 'Артур', 'Валентина', 'Андрей', 'Роман', 'Алина', 'Альберт']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

if len(tutors) > len(klasses):
    klasses += [None for i in range(len(tutors) - len(klasses))]

result = ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
