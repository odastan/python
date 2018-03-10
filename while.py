sum1 = 0
while True:
    number = input ("Введите число")
    if number == "":
        print("Введите число! ")
        continue
    if number <= 0:
        print("Ноль убери ")
    else:
        number = int(number)
        sum1 += number
        print(sum1)

