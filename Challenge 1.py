raw = open("users.txt", "w")
rawcontent = raw.write('''Anderson
Olakunle
Ifeoma
Lee
Margaret
Olakunle
Musa
Musa
Lee
Anderson
Yvonne
Albert
Ofori
Ofori
Rofiyat
Rofiyat
Dele
Muhammed
Rofiyat
Ofori
Lee
Ifeoma''')
raw.close()

edit = open("users.txt", "r")
editcontent = edit.read()
edit.close()

wd = editcontent.split("\n")
wod = list(dict.fromkeys(wd))

new = open("new.txt", "w")
for x in wod:
	y = x + "\n"
	newcontent = new.write(y)
new.close()