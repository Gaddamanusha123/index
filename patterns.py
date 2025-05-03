rows=5
for row in range(1,rows+1):
    s=" "
    for col in range(1,rows+1):
        s+=str(row)+" "
    print(s)

rows = 5
for row in range(1, rows + 1):
    s = ""
    for col in range(row):
        s += str(row) + " "
    print(s)
