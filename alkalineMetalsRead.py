name = []
atomic_number = []
atomic_weight = []

with open('alkaline_metals.txt', 'r') as f:
    for line in f:
        name.append(line.split(' ')[0])
        atomic_number.append(line.split(' ')[1])
        atomic_weight.append(line.split(' ')[2].rstrip())

print(name)
print(atomic_number)
print(atomic_weight)
