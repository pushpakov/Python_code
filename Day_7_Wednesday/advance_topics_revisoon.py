# from a list return a all the element inside a list that's remainder is 0 when divided by 2

given_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

result = filter(lambda x : x % 2 == 0, given_list )
print(list(result))


# using map function to return the square root of each element of the given list 

result1 = map(lambda x : pow(x,2), given_list)

print(list(result1))


# lists compherension
"""
return the numver divided by 3 from the list given using list compherension 
"""

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
list_comp_example = [i for i in given_list if i % 3 == 0]  
print("Output List using list comprehensions:", list_comp_example)  


# dictonary compherension 
dict_output = {i: i**3 for i in given_list if i % 3 == 0}
print("Output Dict using dictionary comprehension:", dict_output)


# set compherension 
set_output = {i for i in given_list if i % 3 == 0}
print("Output Set using list compherensions:" , set_output)

# generator compherension 
generator_output = (i for i in given_list if i%3==0)
for ele in generator_output:
    print ("Output Generator using generator compherenion: ",ele)


# multiple compherensions 
values = [(x,y) for x in range(5) for y in range(3)]  
# is equivalent to the code commented below 
# values = []  
# for x in range(5):  
#     for y in range(3):  
#         values.append((x,y))  
print("result of multiple compherension: ", values)

# nested compherensions
nested_values = [[y*3 for y in range(x)] for x in range(10)]  
# above nested compherension is equivalent to the code commented below 
# nested_values = []  
# for x in range(10):  
#     inner = []  
#     for y in range(x):  
#         inner.append(y*3)  
#         nested_values.append(inner)  
print("result of nested compherension: ", nested_values)


# scope based function 
def func():      
    def local_func():  
        a = 'hello, '  
        b = 'world'  
        return a + b  
    x = 1  
    y = 2  
    return x + y  
print(func())    # to call the parent function 
# to call the inner function we can even create a function to call the inner function or can modify the above code as well



