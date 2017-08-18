# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
rooms=map(int,raw_input().split())
unique_rooms=set(rooms)

print (sum(unique_rooms)*n - sum(rooms))/(n-1)