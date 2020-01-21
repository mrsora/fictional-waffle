# Project Euler 2

firstFib = 1
secondFib = 2

total = 0
totalEven = 0

while total < 4000000:
    total = firstFib + secondFib
    if secondFib % 2 == 0:
        totalEven = totalEven + secondFib
    firstFib = secondFib
    secondFib = total

print(totalEven)

# 4613732
