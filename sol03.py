with open("input03.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

suma = 0
def is_symbol(row, col):
    symbol = False
    if row >= 0 and row < len(lines) and col >= 0 and col < len(lines[row]):
        symbol = (not lines[row][col].isdigit()) and (not lines[row][col] == '.')
    return symbol
j = 0
symbol_near = False
for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        number = ""
        while j < len(lines[i]) and lines[i][j].isdigit():
            number = number + lines[i][j]
            symbol_near = symbol_near or is_symbol(i-1,j) or is_symbol(i+1,j)
            j+= 1
        symbol_after = is_symbol(i-1,j) or is_symbol(i,j) or is_symbol(i+1,j)
        symbol_near = symbol_near or symbol_after 
        if symbol_near and number != "":
            suma += int(number)
        symbol_near = symbol_after
        j+=1

print(suma)

gear_ratios = 0

def get_gear_ratio(row, col):
    coords_list = get_neigh_digits(row, col)
    if  len(coords_list) == 2:
        numbers = get_two_numbers(row, col, coords_list)
        return numbers[0] * numbers[1]
    else:
        return 0

def get_neigh_digits(row, col):
    cnt = 0
    coords = []
    if col > 0 and lines[row][col-1].isdigit():
        cnt += 1 
        coords.append((0,-1))
    if col < len(lines[row])-1 and lines[row][col+1].isdigit():
        cnt += 1 
        coords.append((0,1))
    if row > 0:
        if lines[row-1][col].isdigit():
                cnt += 1
                coords.append((-1,0))
        else:
            if col > 0 and lines[row-1][col-1].isdigit():
                cnt += 1
                coords.append((-1,-1))
            if col < len(lines[row-1])-1 and lines[row-1][col+1].isdigit():
                cnt += 1
                coords.append((-1,1))
    if row < len(lines)-1:
        if lines[row+1][col].isdigit():
                cnt += 1
                coords.append((1,0))
        else:
            if col > 0 and lines[row+1][col-1].isdigit():
                cnt += 1
                coords.append((1,-1))
            if col < len(lines[row+1])-1 and lines[row+1][col+1].isdigit():
                cnt += 1
                coords.append((1,1))
    return coords

def get_two_numbers(row, col, coords):
    numbers = []
    for coord in coords:
        i = row + coord[0]
        j = col + coord[1]
        while j >= 0:
            if lines[i][j].isdigit():
                j -= 1
            else:
                break
        start = j + 1
        j = col + coord[1]
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                    j += 1
            else:
                break
        stop = j
        numbers.append(int(lines[i][start:stop]))
    return numbers



for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (lines[i][j] == '*'):
            gear_ratios += get_gear_ratio(i,j)
            
print(gear_ratios)
