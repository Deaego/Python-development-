import re


def email_parse(email_address):
    d = dict()
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domen>\w+\.\w+)$')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'Электронная почта некорректна: {email_address}')
    return result.groupdict()


print(email_parse('deaego1@yandex.ru'))
print(email_parse('deaego1@yandex.ru'))

