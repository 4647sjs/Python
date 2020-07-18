f=open("sample.txt","r")
lines=f.readlines()
f.close()

sum=0
for line in lines:
    a=int(line)
    sum+=a
avg=sum/len(lines)

f=open("result.txt","a")
f.write(str(avg))
f.close()