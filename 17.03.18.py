def func():
    b = ["Никита", "Рома", "Катя", "Лена", "Дастан", "Кирилл,", "Влад", "Стаc", "Еркебулан"]
    c = [i * 1 for i in range(1, 9+1)]
    d = [i * 1.5 for i in range (1, 9+1)]
    t = input("Введите имя или число: ")
    try:
        t = int(t)
        print(b[t-1])
        print(c[t-1])
        print(d[t-1])
    except:
            for i in range(1, 9+1):
                if t == b[i-1]:
                    print(b[i-1])
                    print(c[i-1])
                    print(d[i-1])
func()
    
 
