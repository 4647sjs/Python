
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
    elif matching_number == 5 and matching_bonus ==0:
        return 1000000
    elif matching_number == 4:
        return 50000
    elif matching_number == 3:
        return 5000



print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))