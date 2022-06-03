PYTHON_CHALLENGE_4 = ''' (Binary Numbers)

Create a program that converts X, an integer (in base 10) to a binary number (in base n), where X and n are integers entered by the user.

The program then displays the solution in the form:

➖➖➖➖➖➖➖➖➖➖➖
3  | 7
	| 2 r 1
	| 0 r 2

:. 7 base 10 = 21 base 3
➖➖➖➖➖➖➖➖➖➖➖'''


X = input("Enter the number (in base 10) whose base is to be changed: ")

n = input("\nEnter the base to be changed to: ")


try:
	if str(X).isnumeric() != True:
		print ("Integer Input is either negative or is not a whole number")
		if X > 0:
			pass
except:
	exit()

try:
	if str(n).isnumeric() == False:
		print ("Base Input is either negative or is not a whole number")
		if X > 0:
			pass
except:
	exit()
	
X = int(X)
n = int(n)
N = X
R = []
T = []

print(f"\n{n} | {X} ")
while X > 0:
	d = int(X/n)
	r = X%n
	R.append(r)
	print(f"  | {d} r {r}")
	X = d

for i in range(1, len(R) + 1):
	T.append(R[-i])
	
f = "".join(map(str, T[0:]))

print (f"\n:. {N} base 10 =  {f} base {n}")