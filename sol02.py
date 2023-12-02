import re

f = open("input02.txt","r")
text = f.read()
f.close()

games = text.split(sep = "\n", maxsplit = 99)
games = [game.split(":")[1].strip() for game in games]

result = 0

red_max = 12
green_max = 13
blue_max = 14

def possible(game):
    pattern = r'[,;]'
    tokens = re.split(pattern, game)
    tokens = [token.strip() for token in tokens]
    for token in tokens:
        if token.find("red") != -1:
            if int(token.split()[0]) > red_max:
                return False
        if token.find("green") != -1:
            if int(token.split()[0]) > green_max:
                return False
        if token.find("blue") != -1:
            if int(token.split()[0]) > blue_max:
                return False
    return True

def power(game):
    pattern = r'[,;]'
    tokens = re.split(pattern, game)
    tokens = [token.strip() for token in tokens]
    min_red = 0;
    min_green = 0;
    min_blue = 0;
    for token in tokens:
        if token.find("red") != -1:
            if (r := int(token.split()[0])) > min_red:
                min_red = r
        if token.find("green") != -1:
            if (g := int(token.split()[0])) > min_green:
                min_green = g 
        if token.find("blue") != -1:
            if (b := int(token.split()[0])) > min_blue:
                min_blue = b
    return min_red * min_green * min_blue

        

for i in range(0, len(games)):
    if possible(games[i]):
        result += (i+1)

print("Result1 = " + str(result))

result2 = 0
for game in games:
    result2 += power(game)


print("Result2 = " + str(result2))
