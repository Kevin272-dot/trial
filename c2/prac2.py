
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


def analyze_data(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text.lower())  # Find all words
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
analyze_data(args.input_file, args.output_file)
