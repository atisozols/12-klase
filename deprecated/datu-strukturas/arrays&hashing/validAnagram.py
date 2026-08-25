s = "sula"
t = "alus"

dictionary1 = {}
dictionary2 = {}

for char in s:
    if char not in dictionary1:
        dictionary1[char] = s.count(char)

for char in t:
    if char not in dictionary2:
        dictionary2[char] = t.count(char)

print(dictionary1) 
print(dictionary2) 
print(dictionary1 == dictionary2)