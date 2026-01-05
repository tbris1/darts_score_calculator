number_of_darts = 3 # number of darts per turn (e.g. 3 darts per turn in a standard game of darts)
turn_list = [n+1 for n in range(number_of_darts)] # covert number_of_darts into list to represent how many darts left within turn 


# input for total score remaining
try: 
    target = int(input("What's your current total? "))
except ValueError: 
    print("This must be an integer.")
    exit()

# input for how many darts left in current turn (1, 2, or 3)
try: 
    darts_left = int(input("How many darts do you have left on this turn? "))
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

# build a list of tuples with viable finishing combinations (i.e. doubles only)
def setup_finishers():
    finishers = []

    for n in range(1, 21):
        finishers.append(("D", n))
    finishers.append(("D", 25))

    return finishers


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

def calculate_setup(target, number_of_darts, options, start_idx=0):
    # returns list of sequences (each sequence being a series of throws)
    # base case = zero remaining darts and target score has been reached
    if number_of_darts == 0:
        return [[]] if target == 0 else []
    # score < 0 is bust
    if target < 0:
        return []

    # for each throw in options, calculate all possible combinations of throw values for following darts that would sum to target
    results = []
    for i in range(start_idx, len(options)):
        throw = options[i]
        v = throw_value(throw)

        tails = calculate_setup(target - v, number_of_darts - 1, options, i)
        for tail in tails: 
            results.append([throw] + tail)

    return results

    



# main function to return possible sequences left 
# final dart must be a double (e.g. if total score is 40, double 20 would is needed)

def calculate(darts_left, current_total):
    if current_total > 170 or current_total < 2:
       # print("N/A")
        return []

    finishers = setup_finishers()
    options = setup_options()

    solutions = []

    # base case - final dart and target is in finishers (i.e. is possible to reach with a double)
    if darts_left == 1:
        for f in finishers:
            if throw_value(f) == current_total:
                return [[f]]
        return []
        
    for finisher in finishers:
        remaining = current_total - throw_value(finisher)

        if remaining < 0:
            continue

        max_setup = min(darts_left - 1, 2)  # never more than 2 setup darts in a 3-dart turn

        for setup_darts in range(0, max_setup + 1):
            setups = calculate_setup(remaining, setup_darts, options, start_idx=0)

            for setup in setups:
                solutions.append(setup + [finisher])

                if len(solutions) == 3:
                    return solutions

    return solutions


print(calculate(darts_left, target))


