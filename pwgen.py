#!/usr/bin/python3

import argparse
import sys
import string
import random

# Create the parse
parser = argparse.ArgumentParser(description="Password generator")

# Add an argument
parser.add_argument('--length', type=int, default=8, help="Password length. Default is 8")

# Parse the argument
args = parser.parse_args()

upperletter1 = random.choice(string.ascii_uppercase)


upperletter2 = random.choice(string.ascii_uppercase)
lowerletter1 = random.choice(string.ascii_lowercase)
lowerletter2 = random.choice(string.ascii_lowercase)
digit1       = random.choice(string.digits)
digit2       = random.choice(string.digits)
symbol1      = random.choice(string.punctuation)
symbol2      = random.choice(string.punctuation)

password = upperletter1 + upperletter2 +\
           lowerletter1 + lowerletter2 +\
           digit1 + digit2 + symbol1 + symbol2

password_list = list(password)
random.shuffle(password_list)

new_password = "".join(password_list)

print(f"Password: {password}")
print(f"New Password: {new_password}")

if (len(new_password) < args.length):
    char_diff = args.length - len(new_password)

    avail_chars = string.ascii_letters + string.digits + \
                  string.punctuation

    print(f"available characters: {avail_chars}")

    new_pw_chars = "".join(random.choices(avail_chars, k=char_diff))

    print(f"new_pw_chars: {new_pw_chars}")


    new_password = new_password + new_pw_chars

print(f"New Password: {new_password}")


