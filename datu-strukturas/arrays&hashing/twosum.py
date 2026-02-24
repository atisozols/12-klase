array = [1, 6, 3, 7, 2, 5]
target = 3

indices = {}

for i in range(len(array)):
    indices[array[i]] = i

print(indices)
for i in range(len(array)):
    print(f"elements: {array[i]}, atrodas pozīcijā: {i}, starpība ar target: {target - array[i]}")
    if target - array[i] in indices:
        print("ir vārdnīcā: ", indices[target - array[i]])

# {1: 0, 6: 1, 3: 2, 7: 3, 2: 4, 5: 5}
# elements: 1, atrodas pozīcijā: 0, starpība ar target: 7
# ir vārdnīcā:  3
# elements: 6, atrodas pozīcijā: 1, starpība ar target: 2
# ir vārdnīcā:  4
# elements: 3, atrodas pozīcijā: 2, starpība ar target: 5
# ir vārdnīcā:  5
# elements: 7, atrodas pozīcijā: 3, starpība ar target: 1
# ir vārdnīcā:  0
# elements: 2, atrodas pozīcijā: 4, starpība ar target: 6
# ir vārdnīcā:  1
# elements: 5, atrodas pozīcijā: 5, starpība ar target: 3
# ir vārdnīcā:  2
