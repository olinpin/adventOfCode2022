with open("./day6/day6.txt", "r") as f:
    file = f.read()

marker = []
i = 0
for i in range(len(file)):
    letter = file[i]
    if letter in marker:
        markerLetter = marker[0]
        while markerLetter != letter:
            markerLetter = marker[0]
            marker.pop(0)
            if letter == markerLetter:
                break
        if letter in marker:
            marker.pop(0)
    marker.append(letter)
    if len(marker) == 4:
        break

print(marker, i+1) # i starts at 0


marker = []
for i in range(len(file)):
    letter = file[i]
    if letter in marker:
        markerLetter = marker[0]
        while markerLetter != letter:
            markerLetter = marker[0]
            marker.pop(0)
            if letter == markerLetter:
                break
        if letter in marker:
            marker.pop(0)
    marker.append(letter)
    if len(marker) == 14:
        break

print(marker, i+1) # i starts at 0