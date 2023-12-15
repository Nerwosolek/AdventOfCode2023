import re

separators = r'[\n,]'
f = open("input15.txt", "r")
text = f.read()
f.close()

text = re.split(separators, text)
text = [item.strip() for item in text if item.strip()]

print(text)
print(len(text))

def hash_string(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash

hashes = []
for t in text:
    hashes.append(hash_string(t))

print(sum(hashes))
print(hash_string("pc"))

boxes = dict()

def find_lens(box, item):
    for i in range(len(box)):
        if box[i][0] == item:
            return i
    return -1

for i in range(256):
    boxes[i] = []

for item in text:
    if item[-1] == '-':
        #delete
        h = hash_string(item[0:-1])
        ind = find_lens(boxes[h], item[0:-1])
        if ind != -1:
            del boxes[h][ind]
    else:
        #add/replace
        label, lens = item.split("=")
        h = hash_string(label)
        ind = find_lens(boxes[h], label)
        if ind != -1:
            #replace
            boxes[h][ind][1] = lens
        else:
            #add
            boxes[h].append([label, lens])

def focusing_power(boxes):
    power = 0
    for b in range(len(boxes)):
        for l in range(len(boxes[b])):
            power += (b+1)*(l+1)*int(boxes[b][l][1])
    return power

print(focusing_power(boxes))



