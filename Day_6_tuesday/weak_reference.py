"""
The reference count usually works as such: each time you create a reference to an object, it is increased by one, and whenever you delete a reference, it is decreased by one.
Weak references allow you to create references to an object that will not increase the reference count.
The reference count is used by python's Garbage Collector when it runs: any object whose reference count is 0 will be garbage collected.
You would use weak references for expensive objects, or to avoid circle references (although the garbage collector usually does it on its own).
"""


res = merge_strings("abc","cda")
print(res)

import weakref
import gc

# dictionary to store some data
# my_dict = {'name': 'Pushpak', 'age': 25}
my_dict = [5,4,6,5]  
class my_dict(dict):
   pass
new_dict = my_dict({'name': 'Pushpak', 'age': 25}) #Use my_list class to define a list
# print(new_dict)

try:
    # Create a weak reference to the dictionary
    my_dict_ref = weakref.ref(new_dict)

    new_weak_list = my_dict_ref()
    # to create a proxy of the weak ref 
    new_proxy = weakref.proxy(new_dict)
    print(new_weak_list)
    print('The object using proxy: ' + str(new_proxy))

    # Check if the weak reference still points to the dictionary
    if my_dict_ref() is None:
        print("The dictionary has been garbage collected")
    else:
        print("The dictionary still exists")

    # Call the __call__() method to get the original object
    original_dict = my_dict_ref()
    print("Original dictionary:", original_dict)

    # Call the __str__() method to get a string representation of the weak reference
    weak_ref_str = my_dict_ref.__str__()
    print("Weak reference string:", weak_ref_str)

    # Call the __repr__() method to get a string representation of the weak reference
    weak_ref_repr = my_dict_ref.__repr__()
    print("Weak reference repr:", weak_ref_repr)

    # Delete the original dictionary
    del my_dict
    # print(my_dict)

    # Call the garbage collector to force garbage collection
    gc.collect()

    # Check if the weak reference still points to the dictionary
    if my_dict_ref() is None:
        print("The dictionary has been garbage collected")
    else:
        print("The dictionary still exists")

except Exception as e:
    print("Exception:", e)


