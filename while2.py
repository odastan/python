sum1 = 0
while True:
    number = input ("Введите число")
    if number == "":
        print("Введите число! ")
        continue
    else:
        number = int(number)
        sum1 += number
        print(sum1)

