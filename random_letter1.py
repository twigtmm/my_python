import random
l=['самовар','весна','лето']
a= random.choice(l)
b=random.choice(a)
lst=list(a)
c=lst.index(b)
lst.insert(c,'?')
lst.remove(b)
    
print(''.join(lst))
d= input("Введите букву: ")
if d==b:
    print("Победа!")
    print("Слово: ",a)
else:
    print("Увы! Попробуйте в другой раз")
    print("Слово: ",a)
