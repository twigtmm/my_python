import numpy

with open('temper.stat', 'r') as file:
    lines = [float(x) for x in [line.strip() for line in file]]
    print("Максимальное значение: ", max(lines))
    print("Минимальное значение: ", min(lines))
    print("Средняя температура: ", numpy.mean(lines))
    print("Кол-во уникальных температур: ", len(set(lines)))
