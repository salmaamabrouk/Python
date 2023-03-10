########################################### QUESTION 1 ###########################################

#def reverse_string(str):
#    reversed_string = str[::-1]
#    print(reversed_string)
#    return reversed_string
#reverse_string("Hello from Salma")

########################################### QUESTION 2 ###########################################

#n1 = float(input("Please enter the first number. "))
#n2 = float(input("Please enter the second number. "))

#sum = n1 + n2
#diff = n1 - n2
#mul = n1 * n2
#quotient = n1 / n2

#print("The sum of ",n1 ,"and ", n2, " is = ", sum)
#print("The difference between ",n1 ,"and ", n2, " is = ", diff)
#print("The multiplication of ",n1 ,"and ", n2, " is = ", mul)
#print("The quotient of ",n1 ,"and ", n2, " is = ", quotient)

########################################### QUESTION 3 ###########################################

#def find_largest_number(numbers):
#    return max(numbers)
#numbers = [10, 13, 28, 1, 17, 82]
#print(find_largest_number(numbers))

########################################### QUESTION 4 ###########################################

#age = int(input("Please enter your age. "))
#if age >= 18:
#    print("You are old enough to vote!")
#else:
#    print("You are not old enough to vote. You need to be 18 or above")

########################################### QUESTION 5 ###########################################

#def longest_word(strings):
#    longest = ""
#    for word in strings:
#        if len(word) > len(longest):
#            longest = word
#    return longest

#strings = ["Lets", "Guess", "The", "Longest", "Word", "In", "This", "List"]
#longest = longest_word(strings)
#print(longest)

########################################### QUESTION 6 ###########################################

#num = float(input("Please enter a number to detect whether it's positive, negative or zero. "))
#if num > 0:
#    print("The number you entered is a positive number")
#elif num < 0:
#    print("The number you entered is a negative number")
#else:
#    print("The number you entered is zero")

########################################### QUESTION 7 ###########################################

#def count_vowels(string):
#    vowels = "AEOUIaeoui"
#    count = 0
#    for char in string:
#        if char in vowels:
#            count += 1
#    return count

#string = "This is string contain vowels"
#print(count_vowels(string))

########################################### QUESTION 8 ###########################################

#sentence = input("Please enter a sentence. ")
#print(sentence.upper())

########################################### QUESTION 9 ###########################################

#def list_even_nums():
#    even_list = []
#    for i in range(10):
#        num = int(input("Please enter 10 integer numbers to extract the even ones. "))
#        if num % 2 == 0:
#            even_list.append(num)
#    return even_list

#even_nums = list_even_nums()
#print("Even numbers: ", even_nums)

########################################### QUESTION 10 ###########################################

#def sort_strings():
#    string_list = input("Please enter a list of strings to sort alphabetically ").split(" ")
#    string_list = [s.strip() for s in string_list]
#    string_list.sort()
#    print("Sorted strings:")
#    for s in string_list:
#        print(s)

#sort_strings()