def find_users(*args):
    file = 'nginx_logs'
    user = []
    d = dict()

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            text = line.split()
            ip = text[0]
            user.append(text[0])
            user.append(text[5].strip('"'))
            user.append(text[6])
            if ip not in d:
                d[ip] = 1
            else:
                d[ip] += 1

            print(user)
            user.clear()
    n = 0
    k = ''
    for key, value in d.items():
        if value > n:
            n = value
            k = key
    print(f'{k, n} Спаммер')


print(find_users())
