import random

# 코드를 작성하세요.
a = random.randint(1, 20)
count = 0
limit = 4
while True:
    if limit ==0:
        print("아쉽습니다. 정답은 %d였습니다."%a)
        break
    b=int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:" %limit))
    limit -= 1
    count += 1
    if b == a:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다."%count)
        break
    elif b < a:
        print("Up")
    else:
        print("Down")

