'''Fibonacci Series
1,1,2,3,5,8,13... and so on
'''

print('Hello, I am Sprint and I would be printing out the fibonacci series for you.')
num=input("How many terms are required in your Fibonacci Series?")
num=int(num)

t1=0
t2=1

for i in range(1,num):
    print(t1,end=' ')
    nt = t1 + t2
    t1 = t2
    t2 = nt



