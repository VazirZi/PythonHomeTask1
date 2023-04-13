# Unit 1

digit = int(input('Введите трехзначное число: '))
sum = 0

if digit < 0: digit *= -1

while digit > 0:
    sum += digit % 10
    digit = int(digit / 10)
print (sum)

# Unit 2

birdCount = int(input('Введите общее количество журавликов: '))
part = birdCount / 3

Katya = part * 2

Petya = part / 2
Sereja = Petya

print(f"Катя сделала {int(Katya)} журавликов, Петя сделал {int(Petya)} журавликов, Сережа сделал {int(Sereja)} журавликов.")