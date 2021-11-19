import sys

with open ('users.csv', 'r', encoding='utf-8') as s1, \
    open('hobby.csv', 'r', encoding='utf-8') as s2, \
    open('users_hobby.txt', 'w', encoding='utf-8') as s3:
    for line1 in s1:
        line2 = s2.readline().strip()
        if not line2:
            line2 = None
        s3.write(f'{line1.strip()}: {line2}\n')
    content = s2.readline()
    if content:
        sys.exit()
