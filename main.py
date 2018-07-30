from perceptron import *
import numpy


def main():
    p = perceptron()
    p.baias = 1
    for i in range(50):
        p.train(numpy.array([0, 0]), 1)
        p.train(numpy.array([1, 0]), 0)
        p.train(numpy.array([0, 1]), 0)
        p.train(numpy.array([1, 1]), 0)

    print(p.calculate([0, 0]))
    print(p.calculate([1, 0]))
    print(p.calculate([0, 1]))
    print(p.calculate([1, 1]))

    print("weights -> ", p.weight)
    print("baias -> ", p.baias)

if __name__ == "__main__":
    main()
