# Exercise 1 : What Are You Learning ? Instructions:
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message(learn):
    print("i am learning how to "+learn)

display_message("code")

# Exercise 2: What’s Your Favorite Book ?Instructions:
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print("One of my favorite book is "+title)

favorite_book("Alice in Wonderland")

# Exercise 3 : Some Geography.Instructions:
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country="Magyarorszag"):
    print(city + " is in "+country)
describe_city("Budapest", "country")

# Exercise 4 : Random.Instructions:
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

def random_number():
    number = (int(input("Please enter a number between 0-100: ")))
    import random
    ran_num = random.randint(0, 100)
    print(ran_num)
    if number == ran_num:
        print("Success! Your Number is: " + str(number) + " and the random number created by the computer is: " + str(ran_num))
    else:
        print("you failed.")

random_number()


# Exercise 5 : Let’s Create Some Personalized Shirts ! Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
def make_shirt(size, print_text):
    print(size, print_text)


make_shirt("Big", "Random text on the shirt")

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
def make_shirt(size="Large", print_text="I love python"):
    print(size, print_text)


make_shirt()

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size, print_text="random text test",):
    print("The size you choosed is: " + size + " And the text you want to print on the shirt is: " + print_text)


make_shirt("Small")
make_shirt("XXL")
make_shirt("Medium", "I am on fire today")

# Bonus: Call the function make_shirt() using keyword arguments.
def make_shirt(size, print_text):
    print(size, print_text)


make_shirt(size="very small", print_text="now i am using keyword argument")

# Exercise 6 : Magicians …Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# magicians_name_list = ["Timea", "Daniel", "Andrey", "Zoltan"]

def show_magicians(magicians_name_list):
    print(magicians_name_list)


show_magicians(magicians_name_list)

# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


def make_great():
    for mag_name in magicians_name_list:
        print(mag_name + " The great")
magicians_name_list = ["Timea", "Daniel", "Andrey", "Zoltan"]


make_great()

show_magicians()












