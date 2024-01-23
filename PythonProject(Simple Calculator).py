#-------------------------------------------------------------------------------
# Name:      Sourav Dutta
# Purpose:
#
# Author:      DELL PC
#
# Created:     02-12-2023
# Copyright:   (c) DELL PC 2023
#------------------------------------------------------------------------------

#Calcuator

#Initializing Value & Operator
digit1 = int(input("Enter 1st Number: "))
digit2 = int(input("Enter 2nd Number: "))
operator = input("Enter any Operator (+,-,*,/): ")

#loop Condition

if operator == '+':
 print(digit1 + digit2)
elif operator == '-':
 print(digit1 - digit2)
elif operator == '*':
 print(digit1 * digit2)
elif operator == '/':
 print(digit1 / digit2)
else:
 print("Invalid")

