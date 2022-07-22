list_data = [i for i in range(1002)]
a = 0
b = 26
for i in range(1, len(list_data)//25+1):
    for j in range(a, b):
        print(j)
    a += 25
    b += 25
