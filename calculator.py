# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae37Hx1J_roBgRlZ7P3iFXnkwwN31ts2
"""

def add(A, B):
       # Function for adding two numbers
       return A + B
    def subtract(A, B):
       # Function for subtracting two numbers
       return A - B
    def multiply(A, B):
       # Function for multiplying two numbers
       return A * B
    def divide(A, B):
       # Function for dividing two numbers
       return A/B
    # Taking input from user
    print ("Select the operation.")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")

    select = input("Enter choice (1/ 2/ 3/ 4): ")

    X_1 = int (input ("Enter the first number: "))
    X_2 = int (input ("Enter the second number: "))

    if select == '1':
       print (X_1, " + ", X_2, " = ", add(X_1, X_2))

    elif select == '2':
       print (X_1, " - ", X_2, " = ", subtract(X_1, X_2))

    elif select == '3':
       print (X_1, " * ", X_2, " = ", multiply(X_1, X_2))
    elif select == '4':
       print (X_1, " / ", X_2, " = ", divide(X_1, X_2))
    else:
       print ("This is an invalid input")