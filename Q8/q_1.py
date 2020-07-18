#jump to python chapter 8

print("q_1")
a="a:b:c:d"
b=a.split(":")
c="#".join(b)
print(a)
print(c)
print("\n")

print("q_2")
a = {'A':90, 'B':80}
print(a.get('C',70))
print("\n")

print("q_3")
print("result is same, but + is create new list, extend is using existing list")
print("\n")

print("q_4")
a=[20,55,67,82,33,90,87,100,25]
result =0
for i in range(len(a)):
    if a[i]>=50:
        result+=a[i]
print(result)
print("\n")

print("q_5")
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-2)+fibo(n-1)
#a=int(input())
a=10
for i in range(a):
    print(fibo(i),end=' ')
print("\n")

print("q-6")
a=input("input number split by ,:")
b=a.split(',')
sum=0
for i in b:
    sum+=int(i)
print(sum)
print("\n")

print("q_7")

print("\n")


