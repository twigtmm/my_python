names = ['John', 'Paul', 'George', 'Ringo']
print(list(filter((lambda x: x== 'John' or x== 'Paul'),names)))
