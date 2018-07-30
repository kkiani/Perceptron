import numpy

class perceptron():
	
	def __init__(self):
		self.weight = numpy.array([0, 0])
		self.baias = 0
		
	def train(self, inVector, out):
		calculated = numpy.dot(self.weight, inVector) + self.baias
		out_c = self.stepUnit(calculated)
		if out_c > out:
			self.weight = numpy.subtract(self.weight, inVector)
		elif out_c < out:
			self.weight = numpy.add(self.weight, inVector)
			
	def calculate(self, inVector):
		out = numpy.dot(self.weight, inVector)
		return self.stepUnit(out)
		
	def stepUnit(self, inVector):
		if inVector > 0:
			return 1
		elif inVector <= 0:
			return 0
		
		
