from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        number = randint(1, 9)
        if number not in numbers:
            numbers.append(number)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    count = 1
    while len(new_guess) < 3:

        a = int(input("%d번째 숫자를 입력하세요:" % count))
        if a > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
            continue
        elif a in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
            continue
        else:
            new_guess.append(a)
            count += 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in guess:
        if i in solution:
            if guess.index(i) == solution.index(i):
                strike_count += 1
            else:
                ball_count += 1
        else:
            pass

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries+=1
    choice = take_guess()
    s, b = get_score(choice,ANSWER)
    print("{}S {}B".format(s,b))
    print("")
    if s==3 and b==0:
        print("축하합니다. %d번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다."%tries)
        break
    else:
        pass