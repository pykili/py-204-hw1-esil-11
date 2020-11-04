for i in 'a'*10:
	line = input()
	letter_1 = line[0]
	for letter_1 in line:
		if (letter_1 == '#') or (letter_1 == '\t'):
			pass
		else:
			tab = 0
			id, form, lemma, smth_else = '', '', '', ''
			for letter in line:
				if letter == '\t':
					tab += 1
				else:
					if tab == 0:
						id += letter
					else:
						if tab == 1:
							form += letter
						else:
							if tab == 2:
								lemma += letter
							else:
								if tab >= 3:
									smth_else += letter
	if form != lemma:
			print(form, lemma)
