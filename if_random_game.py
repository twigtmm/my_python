import random
random_num = random.randint(1,4)
a=int(input("Угадай число!: "))
      
if a == random_num :
    print("Победа")
if ( a > random_num):
    print("Я загадал число меньше твоего")
if ( a < random_num):
    print("Я загадал число больше твоего")
