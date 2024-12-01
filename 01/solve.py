from collections import Counter

list1 = []
list2 = []

with open("input.txt") as input:
    for line in input:
        entry = line.split()
        list1.append(int(entry[0]))
        list2.append(int(entry[1]))

list1.sort()
list2.sort()

distance = 0
similarity = 0

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])
    similarity += list1[i] * Counter(list2)[list1[i]]

print("Distance:", distance)
print("Similarity:", similarity)