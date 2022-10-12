def get_number(num, min, max, next):

    result = ""
    if num !=0:
        if num < 4:
            result = result + min*num 
        elif num == 4:
            result = result + min + max
        elif num < 9:
            result = result + max + min*(num-5)
        else:
            result = result + min + next
    return result

str_in = input()
number_in = int(str_in)

one = number_in % 10
ten = number_in % 100 // 10
hundred = number_in % 1000 // 100
thousand = number_in // 1000

result = ""
result = result + get_number(thousand, "M", "", "")
result = result + get_number(hundred, "C", "D", "M")
result = result + get_number(ten, "X", "L", "C")
result = result + get_number(one, "I", "V", "X")

print(result)
