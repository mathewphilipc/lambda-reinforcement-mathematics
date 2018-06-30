import numpy as np

def reward(R, gamma):
	sum = 0.0
	for i in range(400):
#		print(sum)
		sum += gamma**i
	return R*sum

if __name__ == "__main__":
	print("hello world")
	x = reward(0.5, 10)
	print(x)


