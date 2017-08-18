# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(raw_input())
a=set(map(int,raw_input().split()))
n=int(raw_input())
b=set(map(int,raw_input().split()))

c=a.difference(b)
d=b.difference(a)
e=c.union(d)
for i in sorted(e):
    print i
