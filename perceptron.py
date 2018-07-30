import numpy


class perceptron():
    def __init__(self):
        self.weight = numpy.array([0, 0])
        self.baias = 0

    def train(self, inVector, out):
        out_c = self.calculate(inVector)
        error = out - out_c

        self.weight = numpy.add(self.weight, numpy.dot(error, inVector))
        self.baias = self.baias + error

    def calculate(self, inVector):
        out = numpy.dot(self.weight, inVector) + self.baias
        return self.hardlim(out)


    def hardlim(self, inVector):
        if inVector > 0:
            return 1
        elif inVector <= 0:
            return 0
