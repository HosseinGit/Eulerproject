n=1000
sum=0
for i in range(1,n):
    #print("checking",i)
    if i%3==0 or i%5==0:
        #print(i)
        sum=sum+i
print("sum is",sum)
    #else:
        #print(i,"is false")
