from random import randint
def generate_numbers(n):
    num=[]
    while len(num) < n:
        number = randint(1, 45)
        if number not in num:
            num.append(number)
    return num

print(generate_numbers(6))