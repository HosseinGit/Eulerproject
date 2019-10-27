n=600851475143
#Defining the isprime function
def isprime(f):
    for i in range (2,round(f/2+1)):
        if f%i==0:
            return False
    return True
    print(isprime(f))
    
#finding the prime factors
for i in range(round(n/2+1),2,-1):
    if n%i==0 and isprime(i)==True:
        print('The largest prime factor is',i)
        break
