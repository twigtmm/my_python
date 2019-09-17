value = input("Введите pH: ")
if value:
    pH = float(value)
    if pH == 3:
        print("Литий")
    elif pH==25:
        print("Марганец")
    elif pH==80:
        print("Ртуть")
    elif pH==17:
        print("Хлор")
    else:
        print("Что это?")
    
else:
    print("Введите значение pH!")
