# Metode 1 - hardkoding
for i in range(0,10):
    if(i == 0):
        print('Current number', i, 'Previous number', i, 'Sum', i+(i))
    else:
        print('Current number', i, 'Previous number', i-1, 'Sum', i+(i-1))

# Metode 2 - bruk av variabler
def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print('Current number:', i, ' Previous number:', previousNum, ' Sum:', sum)
        previousNum = i

sumNum(10)