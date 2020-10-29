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


Или:

user_input = input()
b = 0
for character in user_input:
	c = 0
	for a in user_input:
		if a == character:
			c += 1
	if c > b:
		b = c
		most_frequent_character = character
print(most_frequent_character)
