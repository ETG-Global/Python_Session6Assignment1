# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:51:11 2018  @author: krishna.i
Problem Statement 1: Write a function so that the columns of the output matrix are powers of the input
vector. The order of the powers is determined by the increasing boolean argument. Specifically,
when increasing is False, the i-th output column is the input vector raised element-wise
to the power of N - i - 1.
HINT: Such a matrix with a geometric progression in each row is named for Alexandre- Theophile Vandermonde.
"""
import numpy as np

def myColMatrix(x,N,inc=False):        # Custom function to create a matrix 
    if inc:
        Output = np.column_stack([x**i for i in range(N)])
    else:
        Output = np.column_stack([x**(N-i-1) for i in range(N)])
    return Output

myVec = np.array([1,2,3,4,5])       # The input Vector array
myN=5                               # The Variable containing number for column values needed
print("Matrix when Increasing Arg is True:\n", myColMatrix(myVec,myN,True))  # Calling myColMatrix with True argument
print("\n\nMatrix when Increasing Arg is False:\n",myColMatrix(myVec,myN))   # Default Increment value False is Considered
