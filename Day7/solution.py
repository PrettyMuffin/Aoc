from collections import deque


read_from = "input.txt"
ESCAPE_CHAR = "#"

def print_matrix(matrix):
    for row in matrix:
        print(row)

def part1():
    with open(f"./Day7/{read_from}", "r") as file:
        matrix = deque("#" + line.strip() + "#" for line in file.readlines())
        matrix.append(ESCAPE_CHAR * len(matrix[0]))

        S_x, S_y = next((0, i) for i, el in enumerate(matrix[0]) if el == "S")
        Q = deque([(S_x + 1, S_y)]) # immediate down
        viewed_positions = set()
        split_counter = 0
        while Q:
            x, y = Q.popleft()
            print(x,y)
            if (x, y) in viewed_positions:
                continue
            viewed_positions.add((x,y))
            if matrix[x][y] != "^": # go down
                if matrix[x + 1][y] != ESCAPE_CHAR:
                    Q.append((x + 1, y))
                continue
            # split
            right, left = (x, y - 1), (x,  y + 1)
            if right not in viewed_positions:
                Q.append(right)
            if left not in viewed_positions:
                Q.append(left)

            split_counter += 1
        print(split_counter)

def part2():
    with open(f"./Day7/{read_from}", "r") as file:
        matrix = deque("#" + line.strip() + "#" for line in file.readlines())
        matrix.append(ESCAPE_CHAR * len(matrix[0]))
        # Inizializza un array per i conteggi di beam attivi per colonna nella riga corrente
        beam_counts = [0] * len(matrix[0])
        s_col = next(i for i, el in enumerate(matrix[0]) if el == "S")
        beam_counts[s_col] = 1  # un beam parte da S


        for row_idx in range(len(matrix) - 1):  # fino all'ultima riga prima del fondo
            new_beam_counts = [0] * len(matrix[0])
            
            for col, count in enumerate(beam_counts):
                if count == 0:
                    continue
                if matrix[row_idx][col] == "^":  # beam colpisce uno splitter nella riga sotto
                    # split: aggiungi il conteggio a sinistra e destra nella nuova riga
                    if col - 1 >= 0:
                        new_beam_counts[col - 1] += count
                    if col + 1 < len(matrix[0]):
                        new_beam_counts[col + 1] += count
                else:
                    # continua dritto nella stessa colonna
                    new_beam_counts[col] += count
            beam_counts = new_beam_counts
        # Part 2: somma dei beam che raggiungono il fondo
        path_counter = sum(beam_counts)

        print("Path Counter:", path_counter)
# part1()
part2()


