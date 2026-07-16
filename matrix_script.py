# matrix_script.py

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input().replace('\r', '').replace('\n', '')
    matrix.append(matrix_item[:m])

decode_string = "".join(["".join(column) for column in zip(*matrix)])
cleaned_string = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decode_string)
print(cleaned_string)

