import os

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
    if operator not in operators:
        raise ValueError(f"Operatore {operator} non valido")
    if operator == "+":
        total += value
    else:
        total *= value
    return total

def parse_operators(line):
    result = []
    for el in line:
        if el in operators:
            result.append(el)
    return result

def part1():
    with open("./Day6/input.txt", "rb") as file:
        parsed_operators = parse_operators(last_line(file))
        for operator in parsed_operators:
            if operator == "+":
                results.append(0)
            else:
                results.append(1)
        file.seek(0)
        element_read = file.read(4).decode().strip() # leggo un intero
        i = 0
        while element_read:
            if element_read in operators: # letto operatore, basta
                break
            results[i] = operate(results[i], int(element_read), parsed_operators[i])
            if i == len(results) - 1:
                i = 0
            else:
                i += 1
            element_read = file.read(4).decode().strip() # leggo un intero
        print(sum(results))


part1()

