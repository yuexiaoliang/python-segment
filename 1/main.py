import random


def create_file(name, string, number=1000):
    file_name = f'{number}个{name}'
    data = ''
    for _i in range(number):
        data += random.choice(string)

    with open(file_name, mode="w", encoding="utf8") as f:
        f.write(data)



number = '1234567890'
letter = 'qwertyuiopasdfghjklzxcvbnm'
symbol = '!@#$%^&*()-=\\`_+|~{[}]:;\'"<>,./?'
create_file("随机数字.txt", number)
create_file("随机字母.txt", letter)
create_file("随机编程符号.txt", symbol)
create_file("随机编程字符.txt", number + number + letter + letter + symbol)
