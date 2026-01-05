number_of_darts = 3 # number of darts per turn (e.g. 3 darts per turn in a standard game of darts)
turn_list = [n+1 for n in range(number_of_darts)] # covert number_of_darts into list to represent how many darts left within turn 
valid_finishers = [n for n in range(2,41,2)] + [50]
print(valid_finishers)

# input for total score remaining
try: 
    current_total = int(input("What's your current total?"))
except ValueError: 
    print("This must be an integer.")
    exit()

# input for how many darts left in current turn (1, 2, or 3)
try: 
    darts_left = int(input("How many darts do you have left on this turn?"))
    assert darts_left in turn_list
except AssertionError: 
    print(f"This must be an integer between {turn_list[0]} and {turn_list[-1]}")
    exit()

# build a list of tuples with all possible throw combinations in 
def setup_options():
    options = []

    # add singles
    for n in range(1, 21):
        options.append(("S", n))
    options.append(("S", 25)) # to include outer bull (i.e. 25)

    # add doubles
    for n in range(1, 21):
        options.append(("D", n))
    options.append(("D", 25)) # to include inner bull / bullseye (i.e. 50))

    # add trebles
    for n in range(1, 21):
        options.append(("T", n))

    return options

def throw_value(t):
    # takes in one of options and calculates score (e.g. ("D", 18) returns 36)
    kind, n = t 
    if kind == "S":
        return n 
    if kind == "D":
        return n*2 
    if kind == "T":
        return n*3 
    raise ValueError(f"Unknown throw type: {t}")


# main function to return possible sequences left 
# final dart must be a double (e.g. if total score is 40, double 20 would is needed)

def calculate(darts_left, current_total):
    if current_total > 170 or current_total < 2:
       # print("N/A")
        return []

    # base case 
    if darts_left == 1:
        if current_total in valid_finishers:
            # print("Achieveable") 
            if current_total == 50:
                return [[("DBull", )]]
            else:
                return [[("D", current_total // 2)]] 
        return []

print(calculate(darts_left, current_total))


