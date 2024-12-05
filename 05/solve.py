def checkrule(rule, update):
    retval = True

    if (rule[0] in update) and (rule[1] in update):
        retval = update.index(rule[0]) < update.index(rule[1])

    return  retval

def swap(rule, update):
    i = update.index(rule[0])
    j = update.index(rule[1])

    temp = update[j]
    update[j] = update[i]
    update[i] = temp

def getmid(list):
    return list[int((len(list) - 1) / 2)]

def iter(update, rules, func):
    retval = True

    for r in rules:
        retval = func(r, update)
        if retval is False:
            break
    
    return retval

with open("input.txt") as input:

    rules = []
    updates = []
    correct_updates = []
    wrong_updates = []

    for line in input:
        line = line.replace('\n','')
        if '|' in line:
            rules.append(line.split("|"))
        elif len(line) != 0:
            updates.append(line.split(","))

        # Convert from str to int elements
    for i in range(len(rules)):
        for j in range(len(rules[i])):
            rules[i][j] = int(rules[i][j])

    # Convert from str to int elements
    for i in range(len(updates)):
        for j in range(len(updates[i])):
            updates[i][j] = int(updates[i][j])
    
    for u in updates:
        if iter(u, rules, checkrule):
            correct_updates.append(u)
        else:
            x = u
            needscheck = True

            while (needscheck):
                needscheck = False
                for r in rules:
                    retval = checkrule(r, x)
                    if retval is False:
                        swap(r, x)
                        needscheck = True
                        break
            
            wrong_updates.append(x)

    sum = 0
    sum2 = 0

    for u in correct_updates:
        sum += getmid(u)
    
    for u in wrong_updates:
        sum2 += getmid(u)

    print("Sum:", sum)
    print("Sum2:", sum2)
