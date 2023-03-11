########################################### QUESTION 1 ###########################################
#import math

#radius = 5
#area = math.pi * radius ** 2
#print("The area of a circle with a radius of 5 is:", area)

########################################### QUESTION 2 ###########################################

#import my_module

#string = "Hello, world!"
#reversed = my_module.reverse_string(string)
#print(reversed)

########################################### QUESTION 3 ###########################################

#from random import randint

#rand = randint(1, 10)
#print(rand)

########################################### QUESTION 4 ###########################################

#import datetime as dt

#current_dt = dt.datetime.now()
#print(current_dt)

########################################### QUESTION 5 ###########################################

#with open("example.txt") as file:
#    num_of_lines = 0
#    for line in file:
#        num_of_lines += 1

#print("Number of lines in example file is ", num_of_lines, " lines.")

########################################### QUESTION 6 ###########################################

#with open('example.txt', 'r') as file:
#    content = file.read()
#    print(content[::-1])

########################################### QUESTION 7 ###########################################

#with open('example.txt', 'r') as file:
#    content = file.read().replace('\n', '')
#    print(content)

########################################### QUESTION 8 ###########################################

#with open('example.txt', 'r') as read_file:
#    with open('copy.txt', 'w') as write_file:
#        content = read_file.read()
#        write_file.write(content)

########################################### QUESTION 9 ###########################################

#with open('example.txt', 'r') as file:
#    content = file.read().split()
#    longest = max(content, key = len)
#    print(f"The longest word in example file is: {longest}")

########################################### QUESTION 10 ###########################################

#def sum_of_evens():
#    nums = []
#    for i in range(10):
#        num = int(input(f"Enter number {i+1}: "))
#        nums.append(num)

#    even_nums = [num for num in nums if num % 2 == 0]
#    return sum(even_nums)

#sum_even_numbers = sum_of_evens()
#print(f"The sum of all even numbers entered by the user is: {sum_even_numbers}")

########################################### QUESTION 11 ###########################################

#def starts_with_a (words):
#    return [word for word in words if word.startswith('a')]

#words = ["antelope", "lion", "alligator", "cat", "monkey", "cow"]
#filtered_words = starts_with_a(words)
#print(filtered_words)

########################################### QUESTION 12 ###########################################

#def swap_keys_values(input_dict):
#    output_dict = {}
#    for key, value in input_dict.items():
#        output_dict[value] = key
#    return output_dict
#input_dict = {'a': 1, 'b': 2, 'c': 3}
#output_dict = swap_keys_values(input_dict)
#print(output_dict)

########################################### QUESTION 13 ###########################################

#def find_max_min():
#    numbers = input("Please enter 10 numbers separated by spaces: ")
#    numbers = list(map(int, numbers.split()))
#    if len(numbers) != 10:
#        print("Error: Please enter just 10 numbers.")
#        return None
#    max_num = numbers[0]
#    min_num = numbers[0]
#    for num in numbers:
#        if num > max_num:#
#            max_num = num
#        elif num < min_num:
#            min_num = num
#    return (max_num, min_num)
#max_min = find_max_min()
#print(max_min)

########################################### QUESTION 14 ###########################################

#def square_numbers():
#    numbers = input("Please enter 5 numbers separated by spaces: ")
#    numbers = list(map(int, numbers.split()))
#    if len(numbers) != 5:
#        print("Error: Please enter just 5 numbers.")
#        return None
#    squared_numbers = []
#    for num in numbers:
#        squared_numbers.append(num ** 2)
#    return squared_numbers
#squared_numbers = square_numbers()
#print(squared_numbers)

########################################### QUESTION 15 ###########################################

#def combine_lists():
#    input_lists = []
#    for i in range(3):
#        lst = input("Enter list {} of 3: ".format(i+1))
#        lst = list(map(int, lst.split()))
#        input_lists.append(lst)
#    combined_list = []
#    for lst in input_lists:
#        combined_list.extend(lst)
#    return combined_list
#combined_list = combine_lists()

#print(combined_list)

########################################### QUESTION 16 ###########################################

#s = "My name is : "

#def replace_keywords_input(string, **kwargs):
#    for key, value in kwargs.items():
#        string += value
#    return string
#print(replace_keywords_input(s, fname = "Salma ", lname = "Mabrouk"))