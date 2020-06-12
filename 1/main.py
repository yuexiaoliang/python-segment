import random


def create_file(name, string, number=100):
    file_name = f'{number}组{name}'
    data = ''
    for _i in range(number):
        random_num = random.choice(range(3, 10))
        for _j in range(random_num):
            data += random.choice(string)
        data += ' '

    with open(file_name, mode="w", encoding="utf8") as f:
        f.write(data)



number = '1234567890'
letter = 'qwertyuiopasdfghjklzxcvbnm'
symbol = '!@#$%^&*()-=\\`_+|~{[}]:;\'"<>,./?'
create_file("随机数字.txt", number)
create_file("随机字母.txt", letter)
create_file("随机编程符号.txt", symbol)
create_file("随机编程字符.txt", number + number + letter + letter + symbol)
