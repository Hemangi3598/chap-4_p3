# wapp to find factorial of an integer
num = int(input(" enter an integer "))
if num < 0:
	print("invalid integer")
else:
	fact = 1
	for i in range(1, num + 1):
		fact = fact * i
	print(" fact= ", fact)
