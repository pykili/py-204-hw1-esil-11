b = ' '
for i in range (0, 10):
    a = input()
    for i in a:
        if i in b:
            pass
        else:
            b = b + i
print(b)
