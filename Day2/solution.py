import re
import datetime

long_line = ""
with open("./Day2/input.txt", "r") as file:
    long_line = file.readline()

invalid_ids = []

# con regex

def con_regex():
    for ranges in long_line.split(","):
        start, end = ranges.split("-")
        for number in range(int(start), int(end)+1):
            str_number = str(number)
            if re.match(r"^(.+?)\1+$",str_number):
                invalid_ids.append(number)
            # first_half, second_half = str_number[:len(str_number)//2], str_number[len(str_number)//2:]
            # if first_half == second_half:
            #     invalid_ids.append(number)

def senza_regex():
    for ranges in long_line.split(","):
        start, end = ranges.split("-")
        for number in range(int(start), int(end) + 1):
            s = str(number)
            n = len(s)
            
            for d in range(1, n // 2 + 1):
                if n % d == 0 and s[:d] * (n // d) == s:
                    invalid_ids.append(number)
                    break

import time

start = time.time()
con_regex()
end = time.time()

print(f"Regex: {(end - start)*1000:.3f} ms")

start = time.time()
senza_regex()
end = time.time()

print(f"Senza: {(end - start)*1000:.3f} ms")