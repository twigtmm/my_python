sum=0
while True:
    text=input("Введите число или Стоп для выхода: ",)
    
    if text=="Стоп":
          break
    else:
        if text.isalpha():
            print('Ошибка ввода')    
        else:
            sum=sum+int(text)
print(sum)
