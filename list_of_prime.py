a = int(input('Enter number: '))
primenumbers = []
for i in range(2,a+1):
    for j in range(2,i-1):
        if i % j == 0:
            break
    else:
        primenumbers.append(i)
print(primenumbers)