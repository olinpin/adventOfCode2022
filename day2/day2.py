with open("./day2.txt", "r") as f:
    file = f.read()

score_rules = {
    "A": 1,
    "B": 2,
    "C": 3
}

x = file.split("\n")
score = 0
for i in x:
    if i == "":
        continue
    choices = i.split(" ")
    enemy = choices[0]
    me = choices[1]
    if me == "Y":
        me = enemy
    elif me == "Z":
        if enemy == "A":
            me = "B"
        elif enemy == "C":
            me = "A"
        elif enemy == "B":
            me = "C"
    else:
        if enemy == "A":
            me = "C"
        elif enemy == "C":
            me = "B"
        elif enemy == "B":
            me = "A"
    score += score_rules[me]
    if me == enemy:
        score += 3
    elif (me == "B" and enemy == "A") or (me == "A" and enemy == "C") or (me == "C" and enemy == "B"):
        score += 6

print(score)
    
