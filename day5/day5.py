with open("day5/day5.txt", "r") as f:
    file = f.read()

rows = file.split("\n")

i = 0
columns = {}
# put innitial crates to a dictionary
for row in rows:
    split = row.split(" ")
    if "1" in split:
        break
    empty = 0
    cols = 1
    for col in split:
        if col == "":
            empty += 1
            if empty == 4:
                empty = 0
                # if columns.get(cols, None) is None:
                #     columns[cols] = [col]
                # else:
                #     columns[cols].append(col)
                cols += 1
            continue
        if columns.get(cols, None) is None:
            columns[cols] = [col]
        else:
            columns[cols].append(col)
        cols += 1
    i += 1

for i in columns:
    columns[i].reverse()
moveList = []
instructions = rows[i+1:]
for row in instructions:
    if row == "":
        continue
    split = row.split(" ")
    move = int(split[1])
    move_from = int(split[3])
    move_to = int(split[5])
    for _ in range(int(move)):
        moveList.append(columns[move_from][-1])
        columns[move_from].pop()
    for _ in range(int(move)):
        columns[move_to].append(moveList[-1])
        moveList.pop()

res = ""
for i in range(1, len(columns)+1):
    print(i)
    res += columns[i][-1]

print(res.replace("[", "").replace("]", ""))
print(columns)
