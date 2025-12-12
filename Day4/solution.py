
count = 0

matrix: list[str] = []
ESCAPE_CHAR = "#"

# TODO: provare a fare matrice di numeri, che contano quanti adiacenti.
# Part ONE
with open("./Day4/input.txt", "r") as file:
    i = 0
    while current_row:= file.readline().strip():
        if i == 0:
            row_len = len(current_row) + 2
            matrix.append(ESCAPE_CHAR * row_len)
            i = 1
        matrix.append(ESCAPE_CHAR + current_row + ESCAPE_CHAR)
    matrix.append(ESCAPE_CHAR * row_len)

def print_matrix(matrix):
    for i in matrix:
        print(i)

# tot_removed = 0
# can_iterate = True
# current_iteration = 1
# previous_row = matrix[0]
# removed_papers = []
# while can_iterate:
#     current_row = matrix[current_iteration]
#     next_row = matrix[current_iteration + 1]
#     for i in range(1, row_len - 1):
#         if not current_row[i] == "@":
#             continue
#         adj = [(i - 1, previous_row), (i - 1, current_row), (i - 1, next_row), (i, previous_row), (i, next_row), (i + 1, previous_row), (i + 1, current_row), (i + 1, next_row)]
#         tmp_counter = 0
#         for item in adj:
#             if item[1][item[0]] == "@":
#                 tmp_counter += 1
#         if tmp_counter < 4:
#             count += 1
#             removed_papers.append((current_iteration, i))
#             # current_row = current_row[:i] + "x" + current_row[i+1:] 
#     previous_row = current_row

#     if current_iteration + 1 == len(matrix) - 1: # sono arrivato alla fine della matrice
#         if count == 0:
#             can_iterate = False
#         else:
#             for i in removed_papers:
#                 row, column = i
#                 matrix[row] = matrix[row][:column] + "x" + matrix[row][column + 1:] # matrix[row][col] = "x"
#         current_iteration = 1
#         previous_row = matrix[0]
#         removed_papers = []
#         tot_removed += count
#         count = 0
#     else:
#         current_iteration += 1

# print(tot_removed)

# previous_row = ""
# current_row = file.readline().strip()
# while current_row:
#     next_row = file.readline().strip()
#     for i, el in enumerate(current_row):
#         adj = []
#         if not current_row[i] == "@":
#             continue
#         # currentrow[i] == @
#         if not previous_row:
#             if i != 0 and i < len(current_row) - 1:
#                 adj = [(i-1, next_row), (i, next_row), (i + 1, next_row), (i - 1, current_row), (i + 1, current_row)]
#             elif i == len(current_row) - 1:
#                 adj = [(i - 1, next_row), (i, next_row), (i - 1, current_row)]
#             else: # i == 0
#                 adj = [(i, next_row), (i + 1, current_row), (i + 1, next_row)]
#         elif not next_row:
#             if i != 0 and i < len(current_row) - 1:
#                 adj = [(i-1, previous_row), (i, previous_row), (i + 1, previous_row), (i - 1, current_row), (i + 1, current_row)]
#             elif i == len(current_row) - 1:
#                 adj = [(i - 1, previous_row), (i, previous_row), (i - 1, current_row)]
#             else: # i == 0
#                 adj = [(i, previous_row), (i + 1, current_row), (i + 1, previous_row)]
#         else:
#             if i != 0 and i < len(current_row) - 1:
#                 adj = [(i - 1, previous_row), (i - 1, current_row), (i - 1, next_row), (i, previous_row), (i, next_row), (i + 1, previous_row), (i + 1, current_row), (i + 1, next_row)]
#             elif i == len(current_row) - 1:
#                 adj = [(i - 1, previous_row), (i - 1, next_row), (i - 1, current_row), (i, previous_row), (i, next_row)]
#             else: # i == 0
#                 adj = [(i + 1, previous_row), (i + 1, next_row), (i + 1, current_row), (i, previous_row), (i, next_row)]
#         tmp_counter = 0
#         for item in adj:
#             if item[1][item[0]] == "@":
#                 tmp_counter += 1
#         if tmp_counter < 4:
#             count += 1
#     previous_row = current_row
#     current_row = next_row

# print(count)

# SOLUZIONE OTTIMA:
from collections import deque

def neighbors(row, column):
    return [
        (row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
        (row, column - 1),                        (row, column + 1),
        (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)
    ]
Q = deque()
removed = set()
tot_removed = 0
# Le celle che non sono "@" (. o # o x) non influenzano nulla:
# - non possono essere rimosse
# - non diventano mai '@'
# - non hanno vicini che dipendono da loro
# Metterle nella queue sarebbe solo rumore. 
for r in range(1, len(matrix) - 1):
    for c in range(1, row_len - 1):
        if matrix[r][c] == '@':
            Q.append((r, c))
            # -----------------------
            counter = 0
            for nr, nc in neighbors(r, c):
                if matrix[nr][nc] == '@':
                    counter += 1
            if counter < 4:
                tot_removed += 1

print("Parte 1:", tot_removed)

# BFS: per problema di propagazione, riadattato per la propagazione condizionale
tot_removed = 0
while Q:
    r, c = Q.popleft()

    # se già rimosso o non è più '@', skip
    if matrix[r][c] != '@':
        continue

    # conta vicini
    counter = 0
    vicini_utili = set()
    for nr, nc in neighbors(r, c):
        if matrix[nr][nc] == '@':
            counter += 1
            vicini_utili.add((nr, nc))

    # se questo ha meno di 4 vicini → va rimosso
    if counter < 4:
        matrix[r] = matrix[r][:c] + 'x' + matrix[r][c + 1:]
        tot_removed += 1

        # i vicini potrebbero diventare rimovibili
        Q.extend(vicini_utili)


print("Parte 2: ", tot_removed)