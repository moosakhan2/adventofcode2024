import re

# Define the input text // You can adjust the text accordingly
text = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

# Define the regex pattern
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

# Find all matches in the text
matches = re.findall(pattern, text)
print(matches)

# Define the multiplication function
def mul(x, y):
    return x * y

# Initialize variables
pointer = 0
total_sum = 0
evaluate_future_instructions = True

# Iterate through matches and process them
while pointer < len(matches):
    match = matches[pointer]

    if match == "don't()":
        evaluate_future_instructions = False
        pointer += 1
    elif match == "do()":
        evaluate_future_instructions = True
        pointer += 1
    else:
        if evaluate_future_instructions:
            # Evaluate the match 
            total_sum += eval(match)
        pointer += 1

print(total_sum)
