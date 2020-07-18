from random import randint

def generate_numbers(n):
    num=[]
    while len(num) < n:
        number = randint(1, 45)
        if number not in num:
            num.append(number)
    return num


def draw_winning_numbers():
    win_num = generate_numbers(6)
    win_num.sort()
    while True:
        bonus_number = randint(1,45)
        if bonus_number not in win_num:
            win_num.append(bonus_number)
            break
    return win_num

print(draw_winning_numbers())