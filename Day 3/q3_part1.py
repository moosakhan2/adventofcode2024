import re

# You can adjust the input text accordingly
text = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, text)

def mul(x, y):
    return x * y

sum = 0

for i in range(len(matches)):
    sum = sum + eval(matches[i])

print(sum)