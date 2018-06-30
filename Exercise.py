import numpy as np

def reward(gamma, R):
	sum = 0.0
	for i in range(10):
		sum += gamma**i
	return R*sum

if __name__ == "__main__":
	print("hello world")
	x = reward(0.5, 10)
	print(x)


