string = "abcdefghijklmnopqrstuvwxyz" * 10

level = 0
while True:
    if len(string) == 0:
        break
    
    print(string[:level + 1])
    string = string[level + 1:]
    
    level += 1