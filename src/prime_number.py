def finding_factors(Number):
    count = 0

    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
    return count

Num = int(input(" Please Enter any Number: "))

cnt = finding_factors(Num)

if (cnt == 0 and Num != 1):
    print(" %d is a Prime Number" %Num)
else:
    print(" %d is not a Prime Number" %Num)

## SOURCE: https://www.tutorialgateway.org/python-program-to-find-prime-number/