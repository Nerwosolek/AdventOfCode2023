with open("input04.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

print(lines[0])

winning = []
having = []

for line in lines:
    ind1 = line.find(":")
    ind2 = line.find("|")
    winning.append(line[ind1+1:ind2].strip())
    having.append(line[ind2+1:].strip())

print(winning[0])
print(having[0])

points = 0
for i in range(len(having)):
    cnt = 0
    w = winning[i].split()
    h = having[i].split()
    w.sort()
    h.sort()
    print(w)
    print(h)
    for x in h:
        if x in w:
            cnt += 1
    if cnt > 0:
        points += 2 ** (cnt-1)
    print(cnt)
    print(points)
print(points)


cards = 0
copies = [1] * len(having)
for i in range(len(having)):
    cnt = 0
    w = winning[i].split()
    h = having[i].split()
    w.sort()
    h.sort()
    print(w)
    print(h)
    for x in h:
        if x in w:
            cnt += 1
    if cnt > 0:
        a = min(i+1,len(copies))
        b = min(i+cnt,len(copies))
        for j in range(a,b+1):
            copies[j] += copies[i]
    print(cnt)
    print(sum(copies))
print(cards)
