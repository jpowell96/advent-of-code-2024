left = []
right = []

def pairwise_diff(list1, list2):
    zipped = zip(list1, list2)
    paired_diffs = [abs(int(x) - int(y)) for x, y in zipped]    
    total = sum(paired_diffs)
    return total

# Assume lists are sorted
def calc_similarity_score(left, right):
    p1 = 0
    p2 = 0
    # Maybe do a two pointer approach and move the p1 when no more matches
    similarity_score = 0
    occurences = {}

    while (p1 < len(left)):
        if (left[p1] == right[p2]):
            if left[p1] in occurences:
                occurences[left[p1]] = occurences[left[p1]] + 1
            else:
                occurences[left[p1]] = 1
            p2 += 1
        elif (left[p1] < right[p2]):
            p1 += 1
        elif (left[p1] > right[p2]):
            p2 += 1      
    # For key in map
    # occurences[x] * x * occurences
    sum = 0
    for x in left:
        if x in occurences:
            sum += occurences[x] * int(x)
    return sum

with open ('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        split = line.split(" ")
        left.append(split[0])
        right.append(split[3])
left.sort()
right.sort()

print("Final Result: " + str(pairwise_diff(left, right)))
print("Similarity Score: " + str(calc_similarity_score(left, right)))
