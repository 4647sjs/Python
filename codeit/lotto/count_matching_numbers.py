def count_matching_numbers(list_1, list_2):
    set1=set(list_1)
    set2=set(list_2)
    match_count=len(set1&set2)
    return match_count



print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))