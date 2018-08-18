
# ======================
# 18_Hexadecimal.py
# ======================

# Hexadecimal is to base 16, i.e 0 to 15
# represented from 0, then 10 = A, 11 = B etc

# Here is a python program to show numbers in hexadecimal
# the representation for hexadecimal is x

# results from 0 to 17 show from 00 to 0f (15)
# Note that in {0:>2}, first 0 is to pull the first element i in format
# So both {0:>2} and {0:>02x} are pulling same number i

for i in range(16):
    print("{0:>2} in hex is {0:>02x}".format(i))

print()

# Here is an example from 16 to 32

for i in range(16, 32):
    print("{0:>2} in hex is {0:>02x}".format(i))

print()
# Here is an example from 33 to 47

for i in range(33, 48):
    print("{0:>2} in hex is {0:>02x}".format(i))

print()
# How to represent Hexadecimal numbers in python
# To specify a number as hex, we use 0x before it. e.g. 0x20 is a hex number
# From above results, we know that 33 (decimal) is 21 (hexadecimal)
# and 46 (decimal) is 2e hexadecimal

# so we want to represent them in hex numbers

x = 0x21 # This is 33 in decimal
y = 0x2e # This is 46 in decimal

# We can see this prints them in decimal

print(x)
print(y)
print(x * y)

# How to print in hexadecimal

print()
print("{0:02x}".format(x))
print("{0:02x}".format(y))

# Formatting experiment
# we can see that the first values in {0:05} and {1:05} are used to pull elements
# x and y which are in positions 0 and position 1

print()
x = 10000
y = 99999
print(x)
print(y)
print()
print("x is: {0:05} and y is {1:05}".format(x, y))


# How to print in binary
print()
for i in range(16):
    print("{0:>2} in binary is {0:>04b}".format(i))

print()

# From above result, we know that 15 in decimal is equal to 1111 in binary
# Now we can print to convert binary to decimal

for i in range(0b1111):
    print("{0:>04b} in decimal is {0:>02}".format(i))

print()
for i in range(70, 150):
    print("{0:>3} in hex is {0:>03x}".format(i))

# Printing in Octal
# Octal is to increments of 8
# where we go from 000 to 007 and then for 8, it becomes 010


print()
for i in range(0, 15):
    print("{0:>3} in Octal is {0:>03o}".format(i))


# Challenge
# When converting a decimal number to binary, you look for the highest power of 2
# smaller than the number and put a 1 in that column. You then take the remainder
# and repeat the process with the next highest power - putting a 1 if it goes into
# the remainder and a zero otherwise. Keep repeating until you have dealt with all
# powers down to 2 ** 0 i.e. 1

# Write a program that requests a number from the keyboard, then prints out its
# binary representation.

# Obviously, you could use a format string, but that is not allowed for this challenge
# The program should cater for numbers up to 65535 i.e. (2 ** 16) - 1

# Hint: you will need integer division (//) and modulo (%) to get the remainder.
# You will also need ** to raise the number to the power of another.
# for example, 2 ** 8 raises 2 to power 8

# As an optional extra, avoid printing leading zeroes
# Once the program is working, modify it to print Octal rather than binary

# In this section, we have a empty list called powers []
# Then for range from 16 to -1 (since they said 2**16, we get the value 2**power
# Then append it to the empty list to show all the powers in binary.

print("="*20)
powers = []
for power in range(5, -1, -1):
    print("power = {}".format(power))
    powers.append(2 ** power)
    print("powers = {}".format(powers))
print(powers)

print("="*20)

# Here we ask someone to enter their values
# power here is the object to go through list powers.
# so first object is 32768, second is 16384 etc
# For each of these power, we do x (number given) // power
# example if x is 10, first one will be x // 32768, which prints 0 because 10 is
# smaller than 32768
# It iterates through powers until it reaches 8
# Then x//8 is 10//8 gives 1, hence it prints 1
# Then it says x %= power which is x %= 8 meaning x = 10%8 = 2
# So new x is given value of 2 which is the remainder of 10/8
# Then it goes to power 4, 2//4 is 0 (because new x is 2), so it prints 0
# Then new x is 2%4 which is 0 remainder 2, so new x is still 2
# Then it goes to power 2
# Binary digit is 2//2 = 1, so it prints 1
# New x is 2%2 = 0 because there is no remainder
# It goes to power 1
# Binary digit is 0 // 1 = 0, so it prints 0
# There are no more powers to consider.

x = int(input("Please enter a number: "))

for power in powers:
    print("Power is {}".format(power))
    print("Powers are {}".format(powers))
    print("Old x is {}".format(x))
    print("Binary digit = Old x // power =  {0} // {1} = {2}".format(x, power, (x // power)))
    x %= power
    print("New x = Old x % power = {}".format(x))
    print("============")


# how to understand modulus
# x %= 3 is same as x = x%3
# so x %= power is same as x = x%power

print()
x = 10
xMod3 = x%3
print("X is: {}".format(x))
print("xMod3 is {}".format(xMod3))
x %= 3
print(x)

print("="*20)

# An easier way to write above code to print all binary numbers in one line is


powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
# print(powers)

# # Here we ask someone to enter their values

x = int(input("Please enter a number: "))
print("{} in binary form is:".format(x))

for power in powers:
    print(x // power, end='') # we use end='' so it does not go to default newline
    x %= power


# Now for the optional point.
# As an optional extra, avoid printing leading zeroes

print()
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

# Here we ask someone to enter their values

x = int(input("Please enter a number: "))
print("{} in binary form is:".format(x))

printing = False # We initialize variable printing to False

for power in powers:
    bit = x // power # We get the binary bit here
    if bit != 0: # Then test it. if not equal to 0, then we set printing to True
        printing = True
    if printing:  # Here if printing is true (meaning value is not equal to 0)
        print(bit, end='') # we print binary bit and end in a space/ not newline
    x %= power



# Now we need to test boundary numbers, these are the min and max numbers allowed
# Max is 65535 and min is 0
# Max 65535 works fine giving all the binary as ones
# Min 0 gives no results. It should give at least one 0 because 0 is a valid number
# A workaround to this is in our test, we check if bit != 0 or if we are processing
# the last power i.e. power == 1
# Now if we test with zero, we get a binary of 0


powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
# print(powers)

# Here we ask someone to enter their values

x = int(input("Please enter a number: "))
print("{} in binary form is: ".format(x))

printing = False # We initialize variable printing to False

for power in powers:
    bit = x // power # We get the binary bit here
    if bit != 0 or power ==1: #  test bit not 0 or power equal to 1
        printing = True
    if printing:  # Here if printing is true (meaning value is not equal to 0)
        print(bit, end='') # we print binary bit and end in a space/ not newline
    x %= power



# Now we want to convert this program to convert to Octal (8 power)
# Note that binary is 2 power
# We convert to Octal in powers.append(8 ** power)
# Note that octal are in increments of 8
# starts with 0 at 00, to 7 at 07 and then 8 becomes 10 and 9 becomes 11 and so on


powers = []
for power in range(15, -1, -1):
    powers.append(8 ** power) # We use 8 here for octal instead of 2 for binary
print(powers)

# Here we ask someone to enter their values

x = int(input("Please enter a number: "))
print("{} in Octal form is: ".format(x))

printing = False # We initialize variable printing to False

for power in powers:
    bit = x // power # We get the binary bit here
    if bit != 0 or power ==1: #  test bit not 0 or power equal to 1
        printing = True
    if printing:  # Here if printing is true (meaning value is not equal to 0)
        print(bit, end='') # we print binary bit and end in a space/ not newline
    x %= power

