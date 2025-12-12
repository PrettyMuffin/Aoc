current_number = 50;
zero_counter = 0

def isPositive(str: str) -> bool:
    return str[0] == "R"

with open("./Day1/input.txt", "r") as file:
    while read_number:= file.readline().strip():
        delta = int(read_number[1:]) if read_number[0] == 'R' else -int(read_number[1:])
        
        # Prima di aggiornare
        old_bucket = current_number // 100
        new_number = current_number + delta
        new_bucket = new_number // 100
        
        zero_counter += new_bucket - old_bucket  # funziona in entrambi i versi!
        
        current_number = new_number % 100


# lock_current_state = 50
# lock_wrap = 100

# def l(n: int):
#     return (lock_current_state - n) % lock_wrap

# def r(n: int):
#     return (lock_current_state + n) % lock_wrap

# def wraps(value, delta):
#     tmp = value + delta

#     if delta > 0: # r
#         clicks = (tmp // lock_wrap) - (value // lock_wrap)
#     else: # l
#         clicks = ((value - 1) // lock_wrap) - ((tmp - 1) // lock_wrap)

#     return abs(clicks)

# def main():
#     global lock_current_state
#     function_array = {"R" : r, "L": l}
#     counter = 0

#     with open("./Day1/input.txt") as t:
#         for line in t:
#             n = int(line[1::])
#             lock_wrap_count = wraps(lock_current_state, n) if line[0] == 'R' else wraps(lock_current_state, -n)
#             print(f"{lock_current_state} {line[0]} {n} times, which wraps {lock_wrap_count}")
#             counter += lock_wrap_count
#             lock_current_state = function_array[line[0]](n)

#     print(f"answer: {counter}")

# Correct Answer = 6770
print(zero_counter)
# main()