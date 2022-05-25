PYTHON_CHALLENGE_1 = '''
We have a .txt file that contains a list of users who responded to our questionnaire. Our questionnaire could be answered multiple times, so we ended up having duplicated names in our text file, as shown below:

Anderson
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
Ifeoma

Create a file named 'users.txt' that contains the above list of names as is in a directory. (You should be able to select a text or long-press it to copy it from here.)

Now, write a program that removes the excess/duplicate names, and now saves them in a new file named 'new.txt', such that the new file now contains:

Anderson
Olakunle
Ifeoma
Lee
Margaret
Musa
Yvonne
Albert
Ofori
Rofiyat
Dele
Muhammed

Upon verifying that your new file 'new.txt' now contains the specified list above'''


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