def isomorphic(x, y):
    x_counts = {}
    y_counts = {}

    for char in x:
        x_counts[char] = x_counts.get(char, 0) + 1
        
    for char in y:
        y_counts[char] = y_counts.get(char, 0) + 1

    return sorted(x_counts.values()) == sorted(y_counts.values())

def twoSub(array, k):
    answer = []
    indices = {}

    for i in range(len(array)):
        indices[array[i]] = i

    for elem in array:
        if elem + k in indices:
            answer.append([elem, elem + k])
    
    return answer

def netherlands(nums):
    answer = []
    for num in nums:
        if num == 0:
            answer.insert(0, 0)
        elif num == 2:
            answer.append(2)
        else:
            i = 0
            while answer[i] < 1 or i < len(nums):
                i += 1
            answer.insert(i, 1)
        
    print(answer)

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
 
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        print(nums)

s = "ab#c"
t = "ad#c"

def get_output_from_cmd_string(s):
    result = ""
    for char in s:
        if char != '#':
            result += char
        else:
            result = result[:-1]

    return result

print(get_output_from_cmd_string(s) == get_output_from_cmd_string(t))




