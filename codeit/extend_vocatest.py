import random

with open("data/vocabulary.txt" , "r") as f:
    dict1={}
    for voca in f:
        voca_list = voca.strip().split(": ")
        dict1[voca_list[0]] = voca_list[1]

    while True:
        index = random.randrange(0,len(dict1))
        word = list(dict1.keys())[index]
        mean = dict1[list(dict1.keys())[index]]

        a=input("%s:"%word)

        if a == mean:
            print("맞았습니다.")
        elif a == 'q':
            break
        else:
            print("틀렸습니다. 정답은 %s입니다"%mean)
