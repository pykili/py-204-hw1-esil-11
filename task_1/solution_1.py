# your code here
a = input()
n = len(a)
b = int(a[0])
for i in range(0, n):
    if ( int(a[i]) > b):
       b = int(a[i])
    else:
        pass
print (b)
