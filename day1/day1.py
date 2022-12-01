with open("./day1.txt", "r") as f:
    file = f.read()


x = file.split("\n")
res = []
highest = 0
current = 0
for i in x:
    if i != "":
        current += int(i)
    else:
        res.append(current)
        current = 0
res.sort(reverse=True)
print(res[0] + res[1] + res[2])
