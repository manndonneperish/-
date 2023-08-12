# 1
Factor = 1
for i in range(1, 11):
    Factor *= i
print("The factor is {}".format(Factor))

# 6
sum1 = 0
sum2 = 0
sum3 = 0
n = eval(input('enter a number'))
for i in range(1, 11):
    if n % 2 == 1:
        sum1 += n
    else:
        sum2 += n
    sum3 += n
    n = eval(input())
sum3 /= 10
print(sum1, sum2, sum3)

# 7
oddSum = evenSum = cnt = 0
s = input('enter a number:')
while s != 'A':
    cnt += 1
    if int(s) % 2 == 0:
        evenSum += int(s)
    else:
        oddSum += int(s)
    s = input('')
if cnt != 0:
    Mean = (oddSum + evenSum) / cnt
    print(oddSum, evenSum, Mean)
