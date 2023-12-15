f = open("input14.txt", "r")
text = f.read()
f.close()

text = text.split("\n")

text = text[0:-1]

prev_text = text


def bottom_place(column, rock_pos):
    bottom = rock_pos
    for i in range(rock_pos-1, -1, -1):
        bottom = i
        if column[i] == '#' or column[i] == 'O':
            bottom = i + 1
            break
    return bottom

def drop(src_col, src_row, to_row):
    global text
    text[src_row] = text[src_row][:src_col] + '.' + text[src_row][src_col+1:]
    text[to_row] = text[to_row][:src_col] + 'O' + text[to_row][src_col+1:]

for c in range(len(text[0])):
    column = [row[c] for row in text]
    for r in range(len(column)):
        if column[r] == 'O':
            pos = bottom_place(column, r)
            drop(c, r, pos)
            column[r] = '.'
            column[pos] = 'O'


extracted_column = [row[1] for row in prev_text]
print(extracted_column)
extracted_column = [row[1] for row in text]
print(extracted_column)


def points(text):
    points = 0
    for r in range(len(text)):
        points += text[r].count('O') * (len(text) - r)
    return points


print(points(text))


print(prev_text[0:2])
print(text[0:2])

def fall_place(line, rock_pos, dir):
    bottom = rock_pos
    if dir == 'N' or dir == 'W':
        for i in range(rock_pos-1, -1, -1):
            bottom = i
            if line[i] == '#' or line[i] == 'O':
                bottom = i + 1
                break
        return bottom
    elif dir == 'S' or dir == 'E':
        for i in range(rock_pos+1,len(line)):
            bottom = i
            if line[i] == '#' or line[i] == 'O':
                bottom = i - 1
                break
        return bottom

def swap(src_col, src_row, to_col, to_row):
    global text
    text[src_row] = text[src_row][:src_col] + '.' + text[src_row][src_col+1:]
    text[to_row] = text[to_row][:to_col] + 'O' + text[to_row][to_col+1:]

def tilt(dir):
    if dir == 'N':
        for c in range(len(text[0])):
            line = [row[c] for row in text]
            for r in range(len(line)):
                if line[r] == 'O':
                    pos = fall_place(line, r, dir)
                    swap(c, r, c, pos)
                    line[r] = '.'
                    line[pos] = 'O'

    if dir == 'S':
        for c in range(len(text[0])):
            line = [row[c] for row in text]
            for r in range(len(line)-1,-1,-1):
                if line[r] == 'O':
                    pos = fall_place(line, r, dir)
                    swap(c, r, c, pos)
                    line[r] = '.'
                    line[pos] = 'O'

    if dir == 'W':
        for r in range(len(text)):
            line = list(text[r])
            for c in range(len(line)):
                if line[c] == 'O':
                    pos = fall_place(line, c, dir)
                    swap(c, r, pos, r)
                    line[c] = '.'
                    line[pos] = 'O'

    if dir == 'E':
        for r in range(len(text)):
            line = list(text[r])
            for c in range(len(line)-1,-1,-1):
                if line[c] == 'O':
                    pos = fall_place(line, c, dir)
                    swap(c, r, pos, r)
                    line[c] = '.'
                    line[pos] = 'O'


text = prev_text

for i in range(0,1000000):
    tilt('N')
    tilt('W')
    #print(points(text))
    tilt('S')
    tilt('E')
    if i % 1000 == 0:
        print(i,":",points(text))

