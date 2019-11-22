
def nextPrime(n) :
    while(True):
        n +=1
        for j in range(2,n,1) :
            if n%j==0:
                break
        else :
            return n

x = int(input(('Enter number for next prime\n')))
print(nextPrime(x))
