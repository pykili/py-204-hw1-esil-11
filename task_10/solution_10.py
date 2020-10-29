a = input()
n = len(a)
ans = True
for i in range(0, n):
	if a[i] != a[n - i - 1]:
		ans = False
if ans == True:
	print("палиндром")
else:
	print("ловушка, это не палиндром")
