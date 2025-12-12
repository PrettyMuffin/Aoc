import bisect


# La soluzione ancora più ottima sarebbe quella di utilizzare gli interval trees.
# Però devo scaricarmi la libreria....
def solution_part1():
    ranges = []
    numbers = []
    fresh_count = 0
    range_section = True
    with open("./Day5/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                range_section = False
                continue

            if range_section:
                lower, upper = map(int, line.split("-"))
                ranges.append((lower, upper))
            elif line != "":
                numbers.append(int(line))
    # ordino gli intervalli
    ranges.sort()

    # Unisco intervalli sovrapposti
    merged = []
    for lo, hi in ranges:
        # nessuna sovrapposizione
        if not merged or lo > merged[-1][1] + 1:
            merged.append((lo, hi))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
    
    inizi = [lo for lo, _ in merged]

    # Binary search su intervalli
    for x in numbers:
        i = bisect.bisect_right(inizi, x) - 1
        if i >= 0:
            lo, hi = merged[i]
            if lo <= x and x <= hi:
                fresh_count += 1

    print(fresh_count)

def solution_part2():
    ranges = []
    with open("./Day5/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            else:
                lower, upper = map(int, line.split("-"))
                ranges.append((lower, upper))
    # ordino gli intervalli
    ranges.sort()

    # Unisco intervalli sovrapposti
    merged = []
    for lo, hi in ranges:
        # nessuna sovrapposizione
        if not merged or lo > merged[-1][1] + 1: # +1 serve per gli adiacenti, quindi (1, 5) (6, 10) li mergia in uno solo
            merged.append((lo, hi))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))    
    
    sum_fresh = 0
    for lo, hi in merged:
       sum_fresh += hi - lo + 1 # + 1 pk, per esempio 3-5 è composto da {3, 4, 5} -> 3, mentre con 5 - 3 -> 2, quindi devo riportare alla conta per 0
    print(sum_fresh)


# solution_part1()
solution_part2()