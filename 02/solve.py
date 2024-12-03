# Returns true, unless one of the comparisons returns false
def iter(list, compare):
    retval = True

    for i in range(len(list)):
        if i == 0:
            continue
        elif not compare(list[i - 1], list[i]):
            retval = False
            break
    
    return retval

# Return true if increasing
def inc(first,second):
    return first < second

# Return true if decreasing
def dec(first,second):
    return first > second

# Return true if difference is at least 1 and at most 3
def diff(first, second):          
    diff = abs(first - second)
    return diff >= 1 and diff <= 3

def check_list(list):
    retval = False

    # Initial check
    if (list[0] < list[1]): # if initial two are increasing
        if iter(list, inc) and iter(list, diff):
            retval = True
    else: # if initial two are decreasing or equal
        if iter(list, dec) and iter(list, diff):
            retval = True
    
    return retval

safe_reports = 0
safe_reports_dampened = 0

with open("input.txt") as input:
    for line in input:
        entry = line.split()

        # Convert from str to int elements
        for i in range(len(entry)):
            entry[i] = int(entry[i])

        if check_list(entry):
            safe_reports += 1
        else:
            sets = [entry[:i] + entry[i+1:] for i in range(len(entry))]
            for s in sets:
                if check_list(s):
                    safe_reports_dampened += 1
                    break

print("Safe Reports (no dampening):", safe_reports) # Part 1
print("Safe Reports (with dampening):", (safe_reports + safe_reports_dampened)) # Part 2