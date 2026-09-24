def equalisation(a,b,c,d,f):
    try:
        print(f"Пример: ({a}+{b})/({c}-{d}) + {f}**0.5")
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        f = float(f)
        y = (a+b)/(c-d) + (f)**0.5
        print(f"Результат: {y}")
    except ValueError:
        print(f"не тот тип данных")
    except ZeroDivisionError:
        print("Деление на ноль")
