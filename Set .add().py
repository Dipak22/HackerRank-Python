# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
s=set()
for i in range(n):
    s.add(raw_input().strip())
    
print len(s)
    