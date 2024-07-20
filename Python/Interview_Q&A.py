# Question: Write a Python function to reverse a given string.
def reverse_string(intput_string):
    return intput_string[::-1]

# find the largest Number In a List 
def find_largest_number(numbers):
    return max(numbers)

# Check For Palindrome
def is_palindrome(input_string):
    return input_string == input_string[::-1]

# Count Words in a String
def count_words(input_string):
    words = input_string.split()
    return len(words)

#Find the Factorial Of a Number 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Merge Two Sorted Lists 
def merge_sorted_lists(list1 , list2):
    merged_list = sorted(list1 + list2)
    return merged_list

#Find the second Largest(numbers):
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return "List Has Less Than 2 Unique Elements.."
    else:
        return unique_numbers[-2]
    
#Implement A Stack 

class Stack:
    def __init__(self):
        self.items = []    
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack Is Empty"
        
        def top(self):
            if not self.is_empty():
                return self.items[-1]
            else:
                return "Stack Is Empty." 
            
    def is_empty(self):
        return len(self.items) == 0
    
    
# Check For Anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


# Fibonacci Sequence
# - Question: Write a Python function to generate the first N terms of the Fibonacci sequence.
# - Solution:
# python def fibonacci(n): fib_seq = [0, 1] while len(fib_seq) < n: next_term = fib_seq[-1] + fib_seq[-2] fib_seq.append(next_term) return fib_seq[:n]           