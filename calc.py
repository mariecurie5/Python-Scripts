# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse 
import sys

# Create the parser
parser = argparse.ArgumentParser(description= 'Simple Python Calculator')

#Add an  first number argument
parser.add_argument('--number1', type=int, required=True)
parser.add_argument('--number2', type=int, required=True)
parser.add_argument('--operation', type=str, required=True, help="Available values: add, sub, mult")

# Parse the argument
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

def add_numbers(number1, number2):
    sum = number1 + number2
    
    return sum

def subtract_numbers(number1, number2):
    diff = number1 - number2
    
    return diff

def multiplication_numbers(number1, number2):
    product = number1 * number2
    
    return product


if args.operation == 'add':
    sum = add_numbers(args.number1, args.number2)
    
    print(f"{sum}")

if args.operation == 'sub':
    diff = subtract_numbers(args.number1, args.number2)
    
    print(f"{diff}")
    
if args.operation == 'mult':
    product = multiplication_numbers(args.number1, args.number2)
    
    print(f"{product}")
    