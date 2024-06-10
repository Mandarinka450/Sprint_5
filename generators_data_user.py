import random
import string


# Генератор уникального логина
def generate_login_user():
    first_names = ['maksim', 'nastya', 'dasha', 'daniil', 'sasha']
    last_names = ['efimov', 'korotenko', 'sibirskix', 'pashkevich', 'savchenko']
    domains = ['@mail.ru', '@yandex.ru']
    return random.choice(first_names) + random.choice(last_names) + '9' + str(
        random.randrange(100, 999)) + random.choice(domains)


# Генератор уникального пароля
def generate_password_user():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(1, 7))
    return password
