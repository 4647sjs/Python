def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in guess:
        if i in solution:
            if guess.index(i) == solution.index(i):
                strike_count+=1
            else:
                ball_count+=1
        else:
            pass


    return strike_count, ball_count


s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)