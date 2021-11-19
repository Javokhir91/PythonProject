import json

result_dict = dict()

with open('users.csv', 'r', encoding='utf-8') as s1, \
        open('hobby.csv', 'r', encoding='utf-8') as s2:
    for line1 in s1:
        line2 = s2.readline().strip()
        if not line2:
            line2 = None
        if line1 not in result_dict:
            result_dict[line1.strip()] = line2

with open('result.json', 'w', encoding='utf-8') as result_file:
    dict_as_string = json.dumps(result_dict, ensure_ascii=False)
    result_file.write(dict_as_string)
with open('result.json', 'r', encoding='utf-8') as s:
    content= s.read()
    result = json.loads(content)
print(result)