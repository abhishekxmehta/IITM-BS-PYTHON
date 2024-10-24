#LET US FIND THE FACTORIAL OF A NUMBER

print('Enter a number')
n=int(input())

#n=5
#1*2*3*4*5

i=1
answer=1
while(i<=n):
    answer=answer*i
    i=i+1

print(answer)    