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

# Unit 3

numberOfTicket = int(input('Введите номер билета (шестизначное число): '))
count = 0
firstPartOfTicket = 0
secondPartOfTicket = 0

while (count < 6):
    if count < 3:
        secondPartOfTicket += int(numberOfTicket) % 10
        numberOfTicket /= 10
        count += 1
    elif count >= 3:
        firstPartOfTicket += int(numberOfTicket) % 10
        numberOfTicket /= 10
        count += 1

if firstPartOfTicket == secondPartOfTicket:
    print('yes')
else:
    print('no')

# Unit 4

width = int(input('Введите ширину шоколадки (в дольках): '))
height = int(input('Введите длину шоколадки (в дольках): '))

countOfParts = int(input('Введите количество долек для отлома: '))

if width == countOfParts or height == countOfParts:
    print('yes')
elif countOfParts % width == 0 or countOfParts % height == 0:
    print('yes')
else:
    print('no')