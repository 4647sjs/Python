while True:
    v = input("영어 단어를 입력하세요:")
    if v =='q':
        break
    m = input("한국어 뜻을 입력하세요:")
    if m =='q':
        break
    with open("data/vocabulary.txt", "a") as f:
        f.write("%s: "%v)
        f.write("%s\n"%m)