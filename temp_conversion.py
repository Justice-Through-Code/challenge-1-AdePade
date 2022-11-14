
def convert_100_to_celsius():
    fahrenheit = 100
    celsius = (fahrenheit - 32) / 1.8
    print (celsius)
    print('float')
# convert_100_to_celsius()


    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    #this is a float because an INT is a whole number and a float has decimal points

def convert_0_to_celsius():
    fahrenheit = 0
    celsius_0 = (fahrenheit - 32) / 1.8
    print (celsius_0)
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value

# convert_0_to_celsius()

def convert_34_2_to_celsius():
    fahrenheit = 34.2
    celsius = (fahrenheit - 32) / 1.8
    print (celsius)
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables

# convert_34_2_to_celsius()
'''
Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    celisius = 5
    fahrenhiet = (celisius * 1.8) + 32
    print (fahrenhiet)


# convert_5_to_fahrenheit()

def hotter_temp():
    temp1 = (30.2 * 1.8) + 32
    temp2 = (85.1 - 32) / 1.8
    print('30.2 degrees celsius')

# hotter_temp()
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

def convert_fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * (5/9)
    return celsius
    
def convert_celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

print (convert_fahrenheit_to_celsius(100))
print (convert_celsius_to_fahrenheit(32))



