count = int(input("Введите количество: "))
summa = 0
for i in range(1, count + 1):
    number = int(input("Введите число: "))
    summa = number + summa
    
print(summa)
