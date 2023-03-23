# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#range() inbuild function in python for iterating over the range 
# for i in range(-10, -100, -30):
#     print(i)


# #To iterate over the indices of a sequence, you can combine range() and len() as follows:

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#      print(i, a[i])

#break and continue Statements, and else Clauses on Loops

# for n in range(2, 10):
     
#      for x in range(2, n):
#          if n % x == 0:
#              print(n, 'equals', x, '*', n//x)
#              break
#      else:
#          # loop fell through without finding a factor
#          print(n, 'is a prime number')


# for num in range(2, 10):
#      if num % 2 == 0:
#          print("Found an even number", num)
#          continue
#      print("Found a number", num)








# import sys 

# print("Script name:", sys.argv[0])
# print("Arguments:", sys.argv[1:])


# def printAge(name,age):
#     print(f"my name is {name} and age is {age}")   
#     print(name[2:5]) # slicing 
#     print(name[71:])  # need to ask 

# printAge(name="Pushpak",age=199)

# list = [1,2,3,45,8,78] # list is mutable 
# list.append(21) #appending item at the end of the list
# print(list)
# print(len(list))

# fruits = ['apple', 'banana', 'cherry']
# more_fruits = ['orange', 'kiwi', 'pineapple']

# fruits.insert(0,'papaya')
# fruits.pop()
# fruits.remove('banana')
# fruits.reverse()

# x = fruits.copy()
# # x.extend('papaya')
# print(fruits)
# # fruits.extend(more_fruits)


# print(x)



# squares = list(map(lambda x: x**2, range(10)))
# square = [x**2 for x in range(10)]
# print(squares,square)


# x = []
# for y in range(10):
#     x.append(y**2)
# print(x) 


# list = [-4,-2,0,2,4]

# # create a list with value doubled
# y = [x*2 for x in list]
# # print(y) 
# # filter the list to exclude the negative number
# z = [x for x in list if x>=0]
# # print(z) 
# # apply a function to all the elements 
# q = [abs(x) for x in list]
# # print(q)
# # call a method on each element 
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# k =  [weapon.strip() for weapon in freshfruit]
# # print(k)
# # create a list of 2 tuples like (number, square)
# new_list = [(x, x**2) for x in range(6)]
# # print(new_list)
# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# flatten =  [num for elem in vec for num in elem]
# # print(flatten)

# t = 12345, 54321, 'hello!'
# # print(t)


# # SETS
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)

# demonstrate set operations on unique letters from two words 

# a = set('abracadabra')
# b = set('akacazam')

# print(a,b) 

# # letter in a but not in b
# print(a-b)
# # letter in a or b or both
# print(a|b)
# # letter in both a and b
# print(a & b)
# # letter in a or b but not in both 
# print(a^b)

# Dictonary 
tel = {'jack': 4098, 'sape': 4139}

# print(tel)
tel['pushpak'] = 41514

# print(tel)
# del tel['sape']
# print(tel)
# print(list(tel))
# print(sorted(tel))
# print('pushpak' in tel)

# lopping technique 
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
    #  print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

# for i,v in enumerate(knights):
    #  print(i,v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print(q,"...........",a,",,,,,,,,,") 
     print('What is your {0}?  It is {1}.'.format(q, a))
    

# comparison in python 

print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))

















