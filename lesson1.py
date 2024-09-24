'''
name: Delaina Poppleton
Date: 9/16/24
Assignment: Unit 1 Lesson 1 Notes
'''

# Variables

message = "hello, user"
print(message)

# snake_case
user_name = input("enter your name: ")
user_id = int(input("enter your id: "))

# variable type
# print(type(user_name))

# strings
#can use " or ' to indicate string

# f-strings are formatted strings that help with casting string
# way 1 to combine string use
message_one = "welcome" + user_name + "with id" + user_id
print(message_one)

# Way 2 - use f strings
# put variables in curly braces
message_two = f"Welcome {user_name} with ID {user_id}"
print(message_two)

# Possible errors
# apostrophes inside of single quotes
# resolution: use escape sequence \ - tells python next symbol is
# literally that thing, no Pythonic meaning
famous_quotation = 'Quotations are hard to find in the middle \
of lessons - it\'s annoying. Mr. Smith'

# raw strings
mouse = r""" 
 _  _
(o)(o)--.
 \../ (  )
 m\/m--m'`--.
 """
print(mouse)