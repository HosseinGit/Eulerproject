

f_1=1
f_2=2
#print(f_1,f_2)
sum=0
#def fibo(n):
while (f_1<4000000):
    print(f_1)
    f_i=f_2+f_1
    if f_1%2==0:
        sum=sum+f_1

    f_1=f_2
    f_2=f_i
print("sum=",sum)
