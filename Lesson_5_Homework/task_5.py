src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
repeated = []
do_not_repeat = {}

for i in src:
    if i in do_not_repeat:
        do_not_repeat[i] += 1
    else:
        do_not_repeat[i] = 1

result = [el for el in src if do_not_repeat[el] == 1]
print(result)
