a=0
b=1
result=0
n=int(input('enter the no'))
print('the fab. series is')
for i in range (0,n):
    print(a)
    result=a+b
    a=b
    b=result