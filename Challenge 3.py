PYTHON_CHALLENGE_3 = ''' (Factors)

The factors of a number are those lesser (and equal) positive integers that can easily divide a number without giving remainders.

For example, the factors of 6 are 1, 2, 3 and 6.

The factors of 15 are 1, 3, 5 and 15.

Write a program that finds all the factors of a particular given number, N.

The program first takes an input from the user, and raises an exception, if the input is not a positive integer. If the exception is passed, it prints the factors of N.

If for instance, N is given as -8.2, the program raises an exception saying "Wrong input!"

If N is 36, it prints:

➖➖➖➖➖➖➖➖➖➖➖
The factors of 36 are 1, 2, 3, 4, 6, 9, 12, 18 and 36.
➖➖➖➖➖➖➖➖➖➖➖'''

N = input("Enter the integer whose factors is to be found: ") #This line of code takes an input from the user
x = int(N)

try:
	if str(N).isdecimal() != True:
		print ("Wrong Input")
except:
	pass
#The above lines of code(22-33) checks if the input is a positive integer or not and raises an exception, if the input is not a positive integer.

factors = []

for f in range(1, x+1): # This creates a list of numbers ranging from 1 to the integer inputed

	r = x%f # This line of code checks for the remainder when the input integer is divided by each of the numbers from the above list	
	if r == 0:
		factors.append(f) #A list is created for numbers with no remainder (list of factors)
		
f = ", ".join(map(str, factors[0:-1]))

print (f"The factors of {x} are: {f} and {factors[-1]}") #The factors of N is then printed