'''
A XOR gate is a digital logic gate that gives a true (1 or HIGH) output when the number of true inputs is odd

You can build it using an AND gate whose inputs are the output of a NAND gate and the output of an OR gate If a = True and b = False Use logical operators to:

1. Check the output of an OR logic gate and store the value in C

2. Check the output of an AND logic gate and store the value in D

3. Negate the value of D and store the value in D_not

4. Check the output of an AND gate when the inputs are C and D_not

5. Can you do all the steps in one line?

'''
a = True
b = False 
C = a or b
D = a and b
D_not = not D
print(C and D_not)

print((True or False) and (not(True and False)))    #one line
