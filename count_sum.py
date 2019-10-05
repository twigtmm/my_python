x=input('Ввведите число: ',)
sum=0
for i in x:
    if int(i)%2==1:
        sum= sum + pow(int(i),2)

print(sum)
