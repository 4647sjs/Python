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

def count_matching_numbers(list_1, list_2):
    set1=set(list_1)
    set2=set(list_2)
    match_count=len(set1&set2)
    return match_count

def check(numbers, winning_numbers):
    matching_number = count_matching_numbers(numbers, winning_numbers[:6])
    matching_bonus = count_matching_numbers(numbers, winning_numbers[6:])

    if matching_number ==6:
       return 1000000000
    elif matching_number == 5 and matching_bonus == 1:
        return 50000000
    elif matching_number == 5 and matching_bonus == 0:
        return 1000000
    elif matching_number == 4:
        return 50000
    elif matching_number == 3:
        return 5000
    else:
        return 0


