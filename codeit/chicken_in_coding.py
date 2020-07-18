money=0
day=0

with open("data/chicken.txt","r") as f:
    for line in f:
        money+=int(line.strip().split(": ")[1])
        day+=1
avg=money/day
print(avg)