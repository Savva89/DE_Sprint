def bin_sum(x, y):

    x=x[::-1]       
    y=("0"*(len(x)-len(y))+y)[::-1]
    mem = "0"
    result = ""
    
    for number in range(0,len(x)):
        if x[number] == "0" and y[number] == "0":
            result = result + mem
            mem = "0"
        elif x[number] == "1" and y[number] == "1":
            result = result + mem
            mem = "1"
        elif mem == "0":
            result = result + "1"
            mem = "0"
        else:
            result = result + "0"
            mem = "1"

    if mem == "1":
        result = result + mem

    return result[::-1]

x = input()
y = input()[::-1]

x0 = "0"*len(x)
number = 0
result = ""
str_now = ""

for char in y:
    if char == "1":
        str_now = x
    else:
        str_now = x0 

    str_now = str_now + "0"*number

    if result == "":
        result = str_now
    else:
        result = bin_sum(str_now, result)

    number = number + 1

print(result)