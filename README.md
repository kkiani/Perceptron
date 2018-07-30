NOTE: This is not final docs

Simple Perceptron
Overview
This example of using single neural cell show how an perceptron can learn to calculate logic gate (AND, OR , ...).

How to run?
1. First you need to install numpy with pip if you did not befor:
sudo pip install numpy
2. Download full source and extract in a folder.
3. Execute main.py file.

What is Neuron?
Human brain build by network of cells called neuron, these cells are bases for learning process, every cell get N inputs and in core of it self then sum all of them by some weights then only one input would be the output of cell.

Mathematics Model

Perceptron Class 
this class only use numpy library for linear algebra calculation and every thing else is implemented.

structure
	* weight:  
	* bias:

methods
	* __init__
	* train
	* calculate
	* stepUnit
	
License
The MIT License (MIT)

Copyright (c) 2018  Kiarash Kiani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.