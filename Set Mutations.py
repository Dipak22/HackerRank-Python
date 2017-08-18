# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
a=set(map(int,raw_input().split()))
r=input()
for i in range(r):
    op=raw_input().split()
    b=set(map(int,raw_input().split()))
    if(op[0]=='intersection_update'):
        a.intersection_update(b)
    elif(op[0]=='update'):
        a.update(b)
    elif(op[0]=='difference_update'):
        a.difference_update(b)
    elif(op[0]=='symmetric_difference_update'):
        a.symmetric_difference_update(b)
    
print sum(a)