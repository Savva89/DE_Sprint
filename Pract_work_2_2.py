palindrom_string = input()

palindrom_without_space = palindrom_string.replace(' ','')
palindrom_lenght = len(palindrom_without_space) 
palindrom = True

for i in range(0,palindrom_lenght // 2):
    if palindrom_without_space[i] != palindrom_without_space[-(i+1)]:
       palindrom = False
       break 
    
print(palindrom) 