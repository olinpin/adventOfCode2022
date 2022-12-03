def sameInString(firstHalf, secondHalf):
    splitFirst = list(firstHalf)
    for i in splitFirst:
        if i in secondHalf:
            return i
    return None


def sameInThreeStrings(first, second, third):
    splitFirst = list(first)
    for i in splitFirst:
        if i in second and i in third:
            return i
    return None


with open("./day3.txt", "r") as f:
    file = f.read()

x = file.split("\n")
prioritySum = 0
for backpack in x:
    firstHalf = backpack[:int((len(backpack)/2))]
    secondHalf = backpack[int((len(backpack)/2)):]
    same = sameInString(firstHalf, secondHalf)
    if same is None:
        continue
    if same.islower():
        prioritySum += ord(same)-96
    else:
        prioritySum += ord(same)-38

print("Priority sum for first is", prioritySum)

prioritySum = 0
for i in range(0, len(x)-1, 3):
    backpack1 = x[i]
    backpack2 = x[i+1]
    backpack3 = x[i+2]
    same = sameInThreeStrings(backpack1, backpack2, backpack3)
    if same is None:
        continue
    if same.islower():
        prioritySum += ord(same)-96
    else:
        prioritySum += ord(same)-38
