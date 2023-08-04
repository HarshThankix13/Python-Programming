"""
In programming, a "list" is a data structure that stores a collection of items in a specific order. 
Lists are commonly used to hold multiple values, such as numbers, strings, or other objects, in a single variable. 
Lists allow for easy manipulation, traversal, and access of the elements they contain.


In Python, a list is a built-in data type that is created using square brackets [].
Example: my_list = [1, 2, 3, 4, 5].

"""

def reverse_list(lst):
    left , right = 0 , len(lst) - 1 
    while left < right:
        lst[left] , lst[right] = lst[right] , lst[left]
        left += 1
        right -= 1
        
my_list = [1,2,3,4,5] 
reverse_list(my_list)
print(my_list)       

# Remove Last Object From List 

reverse_list = [1,2,3,4,5]
new_list = my_list[:-1]
print(new_list)

# Suppose List 

list1 = [2,33,222,14,25]
"""
list1[0] refers to the first element: 2
list1[1] refers to the second element: 33
list1[2] refers to the third element: 222
list1[3] refers to the fourth element: 14
list1[4] refers to the fifth element: 25
Therefore, list1[-1] refers to the last element: 25

"""

# Append And Extend List Methods

"""
append(): Adds a single element to the end of the list.
extend(): Adds multiple elements from an iterable to the end of the list by unpacking the,
iterable and adding its elements individually.

"""

#--------Append------------
my_list = [1,2,3]
my_list.append(4)
print(my_list)

#--------Extend-----------
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  



#  Python function to get the largest number, smallest num and sum 
# of all from a list.
def analyze_list(numbers):
    if not numbers:
        return None, None, 0  # Return None for both min and max if the list is empty
    
    smallest = min(numbers)
    largest = max(numbers)
    total_sum = sum(numbers)
    
    return smallest, largest, total_sum

# Example usage:
my_list = [34, 12, 67, 23, 9, 51]
smallest, largest, total_sum = analyze_list(my_list)

print("Smallest:", smallest)
print("Largest:", largest)
print("Sum:", total_sum)

# Compare Two List 

list1 = [1,2,3]
list2 = [1,2,3]

if list1 == list2:
    print("The Lists Are Equal...")
else:
    print("The Lists Are Not Equal...")    
    

# Collections Counter

from collections import Counter

list1 = [1,2,3]
list2 = [3,2,1]

if Counter(list1) == Counter(list2):
    print("The Lists Have The Same Elements ") 
else:
    print("The Lists Do Not Have The Same Elements")      
    
    
#Length Of Strings 

def count_strings_with_same_first_last(string_list):
    count = 0
    
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
            
        return count
    
    #Example Usage :
    
    string_list = ["level", "Hello", "Word", "Radar", "Python", "Abba", "Pop"]
    result = count_strings_with_same_first_last(string_list)        
    
    print("Number Of Strings With Same first And Last Character: ", result)
    
    
    
# Duplicates from Lists 

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item) 
        return unique_list
    
    #Example Usage:
    my_list = [1,2,3,3,4,5,5,6,7,7,8] 
    result = remove_duplicates(my_list)
    
    print("Original List : ",my_list) 
    print("List With Duplicates Removed : ", result)    
    
    
#Check Lists Is Empty Or Not 

def is_list_empty(input_list):
    if not input_list:
        return True
    else:
        return False
    
# Example Usage :
empty_list = []
non_empty_list = [1,2,3]

if is_list_empty(empty_list):
    print("The List Is Empty")
else:
    print("The List Is Not Empt.")
    
if is_list_empty(non_empty_list):
    print("The List Is Empty.")
else:
    print("The List Is Not Empty.")
    
    
#True At Least One Common Number 

def have_common_member(list1,list2):
    for item in list1:
        if item in list2:
            return True
        return False
    
#Example Usage :
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

if have_common_member(list1 , list2 ):
    print("The Lists Have At Least One Common Members ")
else:
    print("The Lists Do Not Have Any Common Members ")                            
    
    

# Generate Squares

def generate_square_list(start , end):
    square_list = [x ** 2 for x in range(start, end + 1)] 
    return square_list

#Generate The List Of Squares 
squares  = generate_square_list(1,30)

#Print The First 5 Elements 
print("First 5 Elements :", squares[:5])    

#Print The Last 5 Elements 
print("Last 5 Elements : ",squares[-5:])