from perceptron import *
import numpy

def main():
	p = perceptron()
	p.baias = 0
	for i in range(50):
		p.train(numpy.array([1, 0]), 0)
		p.train(numpy.array([0, 1]), 1)
		p.train(numpy.array([1, 1]), 0)
		p.train(numpy.array([0, 0]), 0)
	
	print(p.calculate([0, 0]))
	print(p.calculate([1, 0]))
	print(p.calculate([0, 1]))
	print(p.calculate([1, 1]))
	
	print(p.weight)
	
if __name__ == "__main__":
	main()
