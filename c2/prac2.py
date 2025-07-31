#!/usr/bin/env python3
"""import argparse
parser = argparse.ArgumentParser(description="a freindly greeting message")
parser.add_argument('name', help="enter a name to greet")
args = parser.parse_args()
print(f"Hello {args.name}")"""

# does the same has the previous
"""import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello {name}!")
else:
    print("Hello there!")"""
# ----------------------------------------------------------------------------------------
import re
import argparse
from re import match
import pandas as pd
import glob


"""def analyze_data(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r"\b\w+\b", text.lower())  
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    with open(output_file, 'w') as f:
        for word, count in word_counts.items():
            f.write(f"{word}: {count}\n")


parser = argparse.ArgumentParser(description='Analyze data from a file.')
parser.add_argument('input_file', help='path to the input file')
parser.add_argument('output_file', help='path to the output file')
arguments = ['input.txt', 'output.txt']  # Replace with your file paths
args = parser.parse_args(arguments)
analyze_data(args.input_file, args.output_file)"""
# -------------------------------------------------------------------------------------
user_input = "999-888-7777"
phone_number = r"^(\d{3})-\d{3}-\d{4}$"
if re.match(phone_number, user_input):
    print(f"{user_input} follows the correct format")
else:
    print(f"{user_input} does not follow the correct format ")
# -------------------------------------------------------------------------------------
"""def validate_email(email):
    valid = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    if re.match(valid, email):
        return True
    else:
        return False


emails = [
    "test@example.com",
    "invalid.email",
    "another_test@domain.co.uk",
    "not_valid@.com",
    "user+123@company.net"
]
for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is not a valid email.")"""
# ------------------------------------------------------------------------------------

# Sample data with inconsistent date formats
"""data = {'date': ['2023-12-31', '12/30/2023', '2023-01-01', '01/02/2023'],
        'category': ['Electronics', 'electronics', 'ELECTRONICS', 'Electronic']}
df = pd.DataFrame(data)

# Standardize date formats
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')
df['date'] = df['date'].fillna(pd.to_datetime(df['date'], format='%Y-%m-%d'))

# Standardize categorical values
df['category'] = df['category'].str.lower()
print(df)"""
# ------------------------------------------------------------------------------------
"""import re

text = "Please contact me at john.doe@example.com or jane.doe@company.org for more information."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

email_matches = re.findall(email_pattern, text)

print(email_matches)"""
# -----------------------------------------------------------------------------------
