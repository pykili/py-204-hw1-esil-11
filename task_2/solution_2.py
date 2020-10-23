a = input()
b = 0
b_ch = ' '
for i in a:
    if a.count(i) > b:
       b = a.count(i)
    else:
        pass
        b_ch = i
print (b_ch)
