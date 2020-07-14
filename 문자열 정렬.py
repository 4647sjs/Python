#문자열 정렬하기
s, n = input().strip().split(' ')
n = int(n)
print('{0:<{1}}'.format(s,n))
print('{0:^{1}}'.format(s,n))
print('{0:>{1}}'.format(s,n))
