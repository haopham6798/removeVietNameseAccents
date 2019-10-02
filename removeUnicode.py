from unidecode import unidecode
def removeVietnameseAccents():
	with open("your_text.txt","r") as f:
		for line in (list(f)):
			removeUnicode = unidecode(line).encode('ascii')
			print(removeUnicode.decode('utf-8'))

removeVietnameseAccents()
