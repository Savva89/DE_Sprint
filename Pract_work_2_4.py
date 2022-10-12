str_in = input()

start_skobka1 = "("
finish_skobka1 = ")"
skobka1 = 0

start_skobka2 = "{"
finish_skobka2 = "}"
skobka2 = 0

start_skobka3 = "["
finish_skobka3 = "]"
skobka3 = 0

for char in str_in:
    if char == start_skobka1: 
        skobka1 = skobka1 + 1
    elif char == finish_skobka1: 
        skobka1 = skobka1 - 1
    elif char == start_skobka2: 
        skobka2 = skobka2 + 1
    elif char == finish_skobka2: 
        skobka2 = skobka2 - 1
    elif char == start_skobka3: 
        skobka3 = skobka3 + 1
    elif char == finish_skobka3: 
        skobka3 = skobka3 - 1

if skobka1 > 0 or skobka2 > 0 or skobka3 > 0:
    print("False")
else:
    print("True")
