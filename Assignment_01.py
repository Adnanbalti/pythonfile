'''                                 Exercise_01:
                            Reverse a list in Python
Given:
list1 = [100, 200, 300, 400, 500]
Expected output:
[500, 400, 300, 200, 100]'''


list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)





'''                                 Exercise_02: 
                    Turn every item of a list into its square
Given a list of numbers. Write a program to turn every item of a list into its square.
Given:
Numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:
[1, 4, 9, 16, 25, 36, 49]'''


a = [1, 2, 3, 4, 5, 6, 7]
square = [a**2 for a in range(1,8)]
print(square)





'''                                 Exercise_03: 
                  Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']'''


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
asd = [x + y for x in list1 for y in list2]
print(asd)






'''                                 Exercise_04: 
                         Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order
and items from list2 in reverse order.
Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:
10 400
20 300
30 200
40 100'''


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)






'''                                 Exercise_05: 
                 Remove all occurrences of a specific item from a list.
Given a Python list, write a program to remove all occurrences of item 20.
Given:
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
[5, 15, 25, 50]'''


list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)


