from collections import deque

def max_list(lista: str, start_indx, end, avoid = set[int]):
    max = lista[start_indx]
    indx = start_indx

    for i in range(start_indx + 1, end):
        if i in avoid:
            continue
        if int(lista[i]) > int(max):
            max = lista[i]
            indx = i
    return (max, indx)


with open("./Day3/input.txt", "r") as file:
    # Part 1
    # while row := file.readline().strip():
    #     max1, indx = max_list(row, 0)
    #     if indx == len(row) - 1:
    #         max2, indx2 = max_list(row, 0, indx)
    #     else: 
    #         max2, indx2 = max_list(row, indx + 1)
    #     if indx2 < indx:
    #         tmp = max1
    #         max1 = max2
    #         max2 = tmp
    #     sum += int(max1 + max2)



    sum = 0
    k = 3  # numero di cifre da rimuovere 
    while row := file.readline().strip():
        removals = len(row) - 12
        stack = []
        
        for d in row:
            # finché possiamo rimuovere e l'ultima cifra nello stack è minore della corrente,
            # rimuoviamo (pop) per migliorare il numero
            while stack and removals > 0 and stack[-1] < d:
                stack.pop()
                removals -= 1
            stack.append(d)

        # Se sono rimaste rimozioni non usate, le applico alla fine (tagliando dalla coda)
        if removals > 0:
            result = "".join(stack[:-removals]) if removals < len(stack) else ""
        else:
            result = "".join(stack)
        sum += int(result)

print(sum, sum == 3121910778619)