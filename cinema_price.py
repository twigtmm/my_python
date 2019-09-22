film= input("Выберите фильм (Пятница, Чемпионы, Пернатая банда): ")
date= input("Выберите дату (Сегодня, Завтра): ")
if film== "Пятница":
    if date == "Завтра":
        time= input("Выберите время (12,16,20): ")
        tickets= int(input("Кол-во билетов: "))
        if tickets > 20:
            if time==12:
                print("Стоимость: ", 0.8*0.95*tickets*250)
            elif time==16:
                print("Стоимость: ", 0.8*0.95*tickets*350)
            else:
                print("Стоимость: ", 0.8*0.95*tickets*450)
        else:
            if time==12:
                print("Стоимость: ", 0.95*tickets*250)
            elif time==16:
                print("Стоимость: ", 0.95*tickets*350)
            else:
                print("Стоимость: ", 0.95*tickets*450)
    else:
         time= input("Выберите время (12,16,20): ")
         tickets= int(input("Кол-во билетов: "))
         if tickets>20:
            if time==12:
                print("Стоимость: ", 0.8*tickets*250)
            elif time==16:
                print("Стоимость: ", 0.8*tickets*350)
            elif time==20:
                print("Стоимость: ", 0.8*tickets*450)
         else:
            if time==12:
                print("Стоимость: ", tickets*250)
                    elif time==16:
                print("Стоимость: ", tickets*350)
                    elif time==20:
                print("Стоимость: ", tickets*450)
elif film == "Чемпионы":
    if date == "Завтра":
        time= input("Выберите время (10,13,16): ")
        tickets= int(input("Кол-во билетов: "))
        if tickets>20:
                if time==10:
                    print("Стоимость: ", 0.8*0.95*tickets*250)
                elif time==13:
                    print("Стоимость: ", 0.8*0.95*tickets*350)
                elif time==16:
                    print("Стоимость: ", 0.8*0.95*tickets*350)
        else:
            if time==10:
                print(print("Стоимость: ", 0.95*tickets*250))
            elif time==13:
                print("Стоимость: ", 0.95*tickets*350)
            elif time==16:
                print("Стоимость: ", 0.95*tickets*350)
    else:
         time= input("Выберите время (10,13,16): ")
         tickets= int(input("Кол-во билетов: "))
         if tickets>20:
            if time==12:
                print("Стоимость: ", 0.8*tickets*250)
            elif time==16:
                print("Стоимость: ", 0.8*tickets*350)
         else:
                print("Стоимость: ", 0.8*tickets*450)


