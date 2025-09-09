import sys
import numpy as np

def _avg(arr):
	print(np.mean(arr))

def _median(arr):
	print(np.median(arr))

def _default():
	print("IDK statistics")

def main():
	if len(sys.argv) == 1:
		_default()
	elif sys.argv[1] == 'mean':
		inarr = [float(x) for x in sys.argv[2:]]
		_avg(inarr)
	elif sys.argv[1] == 'median':
		inarr = [float(x) for x in sys.argv[2:]]
		_median(inarr)

if __name__ == '__main__':
	main()
