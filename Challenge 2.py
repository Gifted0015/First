PYTHON_CHALLENGE_2='''

We have the profiles (first name, middle name, last name) of all registered users on a website written to a variable 'users' as:

users = """Olalade John Adewole
Alimat Faizah Suleman
Ekene James Benson"""

(Notice that the profiles are separated by the line break \n character)

We need to extract only parts of these names for any specified user. (Users are specified by indices 1 - 3).

Write a class named 'profile' that gives the first name, middle name, last name, initials or full name of any of the users.

After creating the class, append your code with the following lines of code:

➖➖➖➖➖➖➖➖➖➖➖
user1 = profile(1)
user2 = profile(2)
user3 = profile(3)

print(user1.user)
print(user2.first)
print(user3.initials)
➖➖➖➖➖➖➖➖➖➖➖

Your output should be:
➖➖➖➖➖➖➖➖➖➖➖
Olalade John Adewole
Alimat
EJB'''



users = """Olalade John Adewole
Alimat Faizah Suleman
Ekene James Benson"""

class profile :
	def __init__ (self, x):
		All_Names = users.split("\n")
		if x == 1:
			self.x = All_Names[0]
		if x == 2:
			self.x = All_Names[1]
		if x == 3:
			self.x = All_Names[2]
	def user (self):
		return self.x
	def first (self):
		Name = self.x.split(" ")
		F = Name [0]
		M = Name [1]
		L = Name [2]
		return F
	def middle (self):
		Name = self.x.split(" ")
		F = Name [0]
		M = Name [1]
		L = Name [2]
		return M
	def last (self):
		Name = self.x.split(" ")
		F = Name [0]
		M = Name [1]
		L = Name [2]
		return L
	def initials (self):
		Name = self.x.split(" ")
		F = Name [0]
		M = Name [1]
		L = Name [2]
		return F[0]+M[0]+L[0]
user1 = profile(1)
user2 = profile(2)
user3 = profile(3)

print(user1.user())
print(user2.first())
print(user3.initials())