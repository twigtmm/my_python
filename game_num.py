import random
b= random.randint(0,10)

print("У вас есть 3 попытки")
count=0
while count<=2:
    text=input("Попробуйте угадать: ",)
    
    if text=="Выход":
        print("Пока!")
        break
    else:
        if int(text)==b:
            print("Победа!")
            break
        else:
                if int(text)>b:
                    print("Попробуйте число меньше!")
                else:
                    print("Попробуйте число больше!")
    count +=1

print("Игра окончена: ",b)
