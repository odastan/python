den = int(input("Введите день"))
month = int (input("Введите месяц"))
god = int (input("Введи год"))

if den <= 31 and den >= 1 :
    print  ("День введен правильно")
else:
    print ("День введен неправильно")

if month <= 12 and month >= 1:
    print ("Месяц введен правильно")
else:
    print ("Месяц введен неправильно")

if god >= 1 and god <= 2018:
    print ("Год введен правильно")
else:
    print ("Год введен неправильно")
