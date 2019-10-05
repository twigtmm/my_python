numbers=[2,4,9,16,25]
func=0
for i in range(len(numbers)):
    numbers[i]=pow(numbers[i],2)
print(numbers)

def f(x):
    return pow(x,2)
print(list(map(f,[2,4,9,16,25])))

a=[]
for i in range(5):
    new_element=int(input())
    new_element=pow(new_element,2)
    a.append(new_element)
print(a)
