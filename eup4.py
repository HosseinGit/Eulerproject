
def ispalindromic(number):
    a=str(number)
    l=len(a)
    if l%2==0:
        part_1=a[0:int(l/2)]
        part_2=a[int(l/2):]
        if part_1==part_2[::-1]:
            return True
        else:
            return False
    else:
        part_1=a[0:int(l/2)]
        part_2=a[int(l/2)+1:]
        if part_1==part_2[::-1]:
            return True
        else:
            return False
#print(ispalindromic(27102))
#    else:
upper_limit =0
n=2
for i in range(1, n+1):
    print(i)
    upper_limit =upper_limit * 10
    print(upper_limit)
    upper_limit =upper_limit + 9

    print(upper_limit)
