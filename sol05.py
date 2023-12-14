import sys

f = open("input05.txt", "r")
text = f.read()
f.close()

text = text.split("\n")

print(text)

i = 0
l = 0
maps = []
if text[i].startswith("seeds:"):
    seeds = text[i].split()[1:]
    seeds = [int(s) for s in seeds]

seeds_ranges = []
for i in range(0,len(seeds),2):
    seeds_ranges.append([seeds[i],seeds[i+1]])
seeds_ranges = sorted(seeds_ranges, key = lambda k: k[0])

print(seeds,"Len:",len(seeds))

i = text.index("seed-to-soil map:")-1
for l in range(0,7):
    i += 2
    mapa = []
    while text[i] != '':
        mapa.append([int(n) for n in text[i].split()])
        i += 1
    mapa = sorted(mapa, key = lambda x: x[1])
    maps.append(mapa)

def get_mapped_value(val, mapa):
    if val < mapa[0][1]:
        print("-1")
        return val
    else:
        for i in range(0,len(mapa)):
            if mapa[i][1] > val:
                break
#        print(i)
        if mapa[i-1][1]+mapa[i-1][2]-1<val:
            return val
        else:
            val = mapa[i-1][0] + (val - mapa[i-1][1])
    return val

def get_last_map(seed):
    value = seed
    for m in range(0, len(maps)):
        value = get_mapped_value(value, maps[m])
        print(m,":",value)
    return value

minimal = (sys.maxsize, -1)
for seed in seeds:
    m = get_last_map(seed)
    print("Seed:",seed,"last:",m)
    if m < minimal[0]:
        minimal = (m, seed)

print("minimum:",minimal[0])


def map_range(ranges, map):
    m = 0
    mk = 0
    input_map = []
    for range in ranges:
        start = range[0]
        length = range[1]
        end = start + length - 1
        left = start
        while left <= end:
            while m < len(map) and (left >= map[m][1] and left >= map[m][1] + map[m][2] - 1):
                m += 1
            if (m >= len(map)):
                right = end
            elif left < map[m][1]:
                right = min(map[m][1], end)
            elif left < map[m][1] + map[m][2] - 1:
                right = min(map[m][1] + map[m][2] - 1, end)
            input_map.append([left, right - left + 1])
            left = right + 1
    return(input_map)

next_range = seeds_ranges
for map in maps:
    next_range = map_range(next_range, map)
    for r in range(len(next_range)):
        next_range[r][0] = get_mapped_value(next_range[r][0], map)
    next_range = sorted(next_range, key = lambda x: x[0])

print("---------------------------------------")

            
for m in range(len(next_range)-1):
    print(m,":", next_range[m+1][0] - (next_range[m][0] + next_range[m][1] - 1),"\t", next_range[m])
