import os
from math import prod
from collections import deque
import itertools

operators = {"*", "+"}
results = []

def last_line(file):
    if file.mode != "rb":
        raise ValueError("Il file deve essere aperto con 'rb'.")
    try:
        file.seek(0, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)
    except OSError:
        file.seek(0)
    return file.readline().decode().strip()


def operate(total: int, value: int, operator: str):
    return total + value if operator == "+" else total * value

def parse_operators(line):
    return [(i, c) for i, c in enumerate(line) if c in operators]

def print_matrix(matrix):
    for line in matrix:
        print(line)

def part1():
    with open("./Day6/input.txt", "r") as file:
        lines = file.read().splitlines()
        parsed_operators = parse_operators(lines.pop())
        results = [0 if op == "+" else 1 for op in parsed_operators]
        i = 0
        for line in lines:
            for num in line.split():
                if num:
                    results[i] = operate(results[i], int(num), parsed_operators[i])
                    i = (i + 1) % len(results)

        print(sum(results))



def part1_pythonica():
    with open("./Day6/test_input.txt", "r") as file:
        lines = file.read().splitlines()
        parsed_operators = parse_operators(lines.pop())
        op_indx = [i for i, _ in parsed_operators]
        op_indx.append(len(lines[0]))
        slices = [(start, end) for start, end in itertools.pairwise(op_indx)]
        matrix = [
            [
                int(line[start: end].replace(" ", "")) 
                for start, end in slices
                
            ]
            for line in lines
        ]
        columns = zip(*matrix)
        tots = [
            sum(col) if op == "+" else prod(col)
            for col, (_, op) in zip(columns, parsed_operators) 
        ]
        print(sum(tots))



def part2():
    file = open("./Day6/input.txt", "r")
    lines = file.read().splitlines()
    parsed_operators = parse_operators(lines.pop())
    file.close()

    matrix = []

    for line in lines:
        i = 1
        prev_indx = parsed_operators[0][0]
        j = 0
        matrix_row = []
        while j < len(line):
            if i < len(parsed_operators):
                indx = parsed_operators[i][0]
            else:
                indx = len(line)
            matrix_row.append(int(line[prev_indx: indx - 1 if indx < len(line) else indx].replace(" ", "0")))
            j += indx - prev_indx
            i += 1
            prev_indx = indx
        matrix.append(matrix_row)


    results = [0 if op[1] == "+" else 1 for op in parsed_operators]
    div = 10

    for col in range(len(matrix[0])):
        zero_counter = 0
        while zero_counter < len(matrix):
            value = ""
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    continue

                value += str(matrix[row][col] % div) if matrix[row][col] % div != 0 else ""
                matrix[row][col] //= div
                if matrix[row][col] == 0:
                    zero_counter += 1
            results[col] = operate(results[col], int(value), parsed_operators[col][1])

    return sum(results)

def part2_pythonica():
    file = open("./Day6/input.txt", "r")
    lines = file.read().splitlines()
    parsed_operators = parse_operators(lines.pop())
    file.close()

    indx = [i for i, _ in parsed_operators]
    indx.append(len(lines[0]))
    matrix = [
        [
            line[indx[i-1]: el - 1 if i < len(indx) - 1 else el].replace(" ", "0")
            for i, el in enumerate(indx)
            if i != 0
        ] 
        for line in lines
    ]

    from math import prod

    columns = list(zip(*matrix))
    tot_values = deque()
    def evaluate(lista: list[int], op):
        return sum(lista) if op == "+" else prod(lista)
    # for i, col in enumerate(columns):
    #     numeri_verticali = list(zip(*col)) # stampa i numeri in maniera vertiale
    #     numbers = [int("".join(el).replace("0",'')) for el in numeri_verticali]
    #     tot_values[i] = evaluate(numbers, parsed_operators[i][1])
    for col, (_, op) in zip(columns, parsed_operators):
        numeri_verticali = list(zip(*col)) # stampa i numeri in maniera vertiale
        numbers = [int("".join(el).replace("0",'')) for el in numeri_verticali]
        tot_values.append(evaluate(numbers, op))
    return sum(tot_values)

# part1()

import time
start = time.perf_counter()
sol1 = part2()
end = time.perf_counter()
print("La soluzione in stile C è: ", end - start)

start = time.perf_counter()
sol2 = part2_pythonica()
end = time.perf_counter()
print("La soluzione pythonica è ", end-start)

assert(sol1 == sol2)