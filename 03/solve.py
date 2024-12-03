import re

def isdo(text):
    return re.search('do\(\)', text)

def isdont(text):
    return re.search('don\'t\(\)', text)

def runcode(instructions):
    product = 0
    doit = True
    
    for i in instructions:
        if isdo(i):
            doit = True
        elif isdont(i):
            doit = False
        elif doit:
            values = re.findall(r'\d+', i)
            product += int(values[0]) * int(values[1])
    
    return product

with open("input.txt") as input:
    code1 = []
    code2 = []
    instructions1 = []
    instructions2 = []
    product = 0

    for line in input:
        code1.append(re.findall('mul\([0-9]+,[0-9]+\)', line)) # Part 1
        code2.append(re.findall('do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\)', line)) # Part 2

    for l in code1:
        for i in l:
            instructions1.append(i)

    for l in code2:
        for i in l:
            instructions2.append(i)

    print("Product 1:", runcode(instructions1))
    print("Product 2:", runcode(instructions2))