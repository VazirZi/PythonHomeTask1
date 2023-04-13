# Unit 1

digit = int(input('Введите трехзначное число: '))
sum = 0

if digit < 0: digit *= -1

while digit > 0:
    sum += digit % 10
    digit = int(digit / 10)
print (sum)