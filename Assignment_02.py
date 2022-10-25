'''                               Question_01
Find the positions of:
elements in x where its value is more than its corresponding element in y, and
elements in x where its value is equals to its corresponding element in y.
Start with these:

x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])

Desired output:
(array([1, 2, 4, 5, 6, 7, 8, 9]),) and (array([0]),)'''


import numpy as np

x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])

print(np.where(x > y))
print(np.where(x == y))


'''                               Question_02
Generate a 1-D array of 10 random integers. Each integer should be a number between 30 and
40 (inclusive)

Sample of desired output:
[36, 30, 36, 38, 31, 35, 36, 30, 32, 34]
Your answer may contain different values but should fulfill the question requirements.'''


num1 = np.random.randint(33, 40, size = (10))

print(num1)


'''                               Question_03
Replace all odd numbers in the given array with -1
Start with:
exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

Desired output:
[ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1]'''


num2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
num2[num2 % 2 == 1] = -1

print(num2)
