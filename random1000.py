from random import randint
numbers = []


for i in range(1000):
        numbers.append(randint(-100, 100))

def find_count(numbers):
    smallest = min(numbers)
    minindex= numbers.index(smallest)
    biggest = max(numbers)
    maxindex= numbers.index(biggest)
    if maxindex > minindex:
        count= maxindex-minindex +1
    else:
        count = minindex- maxindex +1
    return (count)
    
print(find_count(numbers))
