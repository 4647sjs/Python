def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    count=1
    while len(new_guess)<3:

        a=int(input("%d번째 숫자를 입력하세요:"%count))
        if a > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
            continue
        elif a in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
            continue
        else:
            new_guess.append(a)
            count+=1

    return new_guess

print(take_guess())