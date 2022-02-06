my_list = [i ** 3 for i in range(1, 1001, 2)]
my_list_2 = []
num = 0
for i in my_list:
    num_1 = i
    num_2 = (num_1 // 100000000) % 10
    num_3 = (num_1 // 10000000) % 10
    num_4 = (num_1 // 1000000) % 10
    num_5 = (num_1 // 100000) % 10
    num_6 = (num_1 // 10000) % 10
    num_7 = (num_1 // 1000) % 10
    num_8 = (num_1 // 100) % 10
    num_9 = (num_1 // 10) % 10
    num_10 = num_1 % 10
    if (num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10) % 7 == 0:
        my_list_2.append(i)
final = sum(my_list_2)
print(final)



