time = int(input("Время: "))

if time >= 1 and time <= 5:
           print("Ночь")

elif time >= 6 and time <= 11:
           print("Утро")

elif time == 12:
           print("Полдень")

elif time >= 13 and time <= 16 :
           print("Обед")

elif time >=17 and time <=23:
           print("Вечер")

elif time == 24:
           print("Полночь")           

print("bye")
