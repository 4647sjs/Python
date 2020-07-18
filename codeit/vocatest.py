with open("data/vocabulary.txt","r") as f:
    for voca in f:
        voca_list=voca.strip().split(": ")
        a=input("%s:"%voca_list[0])

        if a==voca_list[1]:
            print("맞았습니다.")
        else:
            print("틀렸습니다. 정답은 %s입니다"%voca_list[1])