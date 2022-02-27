import sys
import json

result_d = dict()
with open('user.csv', 'r', encoding='utf-8') as f1, \
        open('hobby.csv', 'r', encoding='utf-8') as f2:
    for line_1 in f1:
        line_2 = f2.readline().strip()
        if not line_2:
            line_2 = None
        if line_1 not in result_d:
            result_d[line_1.strip()] = line_2
    content = f2.read()
    if content:
        sys.exit(1)
with open('result.json', 'w', encoding='utf-8') as result:
    dict_string = json.dumps(result_d, ensure_ascii=False)
    result.write(dict_string)
with open('result.json', 'r', encoding='utf-8') as f:
    content = f.read()
    final_result = json.loads(content)
print(final_result)
