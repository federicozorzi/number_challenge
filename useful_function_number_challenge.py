# useful functions to play the 20 number challenge

def find_possible_spots(v, r:int):
    pos_start = 0
    pos_stop = len(v) - 1

    # check if r is in v
    if r in v:
        return -2, -2

    # i go through all the positions in v to find if each specific position can be pos_start or pos_stop
    for j in range(len(v)):
        if v[j] < r:
            pos_start = j+1
        if v[- 1 - j] > r:
            pos_stop = len(v) -1 - j -1

    return pos_start, pos_stop

def insert_number(v, r, pos_start, pos_stop, min_value, max_value, verbosity = 0):
    if pos_start == -2 and pos_stop == -2:
        if verbosity > 0:
            print(f"{r} is in v, skip number")
        return 0, v
    if pos_start == len(v): #and so there are no slots available as r is bigger than the value in position len(v) - 1
        if verbosity > 0:
            print(f"{r} is greater than {v[-1]}, the number in the last spot")
        return -1, v
    if pos_stop == -1: # and so r is lower than the value in position 0 of v
        if verbosity > 0:
            print(f"{r} is lower than {v[0]}, the number in the first spot")
        return -1, v
    if pos_stop - pos_start + 1 <= 0:
        if verbosity > 0:
            print(f"There are no spots available for number {r} in {v}")
        return -1, v
    else: #game on, we want to insert the number in v
        pos = find_spot(v, r, pos_start, pos_stop, min_value, max_value)
        v[pos] = r
        return 1, v

# algorithm: still to determine if it's working at its best when inserting min and max values
def find_spot(v, r, pos_start, pos_stop, min_value, max_value):
    pos = -1
    k = -1

    start = min_value
    stop = max_value

    if pos_start != 0:
        start = v[pos_start -1]
    if pos_stop != len(v) -1:
        stop = v[pos_stop +1]

    #possible ranges
    n_spots = pos_stop - pos_start + 1
    if stop == max_value:
        stop = max_value+1
    ranges_per_spot = split(start, stop, n_spots)

    for j, ran in enumerate(ranges_per_spot):
        if r in ran:
            k = j
    if k==-1:
        raise Exception(f"Error: algorithm fails to insert {r} in {v} between positions {pos_start} and {pos_stop}")
    else:
        pos = pos_start + k
    return pos

def split(a, b, n):
    a = int(a)
    b = int(b)
    l = range(a, b)
    k, m = divmod(len(l), n)
    return (l[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))