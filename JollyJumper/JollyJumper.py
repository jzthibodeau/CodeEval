import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	isJumper = True
	line = test.split(" ")
	length = len(line)
	for i in range(0, len(line)):
		if i +1 >= len(line) or len(line) == 1:
			break
		else:
			if abs(int(line[i]) - int(line[i+1])) == (length-1):
				length -= 1
			else:
				isJumper = False
				break
	if isJumper == True:
		print("Jolly")
	else:
		print("Not jolly")

test_cases.close()
