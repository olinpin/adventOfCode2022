with open("./day4.txt", "r") as f:
    file = f.read()

pairs = file.split("\n")

contain = 0

for pair in pairs:
    if pair == "":
        continue
    p = pair.split(",")
    first = p[0].split("-")
    second = p[1].split("-")
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        contain += 1
    elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        contain += 1


overlap = 0

for pair in pairs:
    if pair == "":
        continue
    p = pair.split(",")
    first = p[0].split("-")
    second = p[1].split("-")
    if int(first[0]) in range(int(second[0]), int(second[1])+1):
        overlap += 1
    elif int(first[1]) in range(int(second[0]), int(second[1])+1):
        overlap += 1
    elif int(second[0]) in range(int(first[0]), int(first[1])+1):
        overlap += 1
    elif int(second[1]) in range(int(first[0]), int(first[1])+1):
        overlap += 1

print(overlap)
