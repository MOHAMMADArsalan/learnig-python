num_1 = input("Enter First Number: ")
num_2 = input("Enter Second Number: ")
operator = input("Operator: ")

num_1 = float(num_1)
num_2 = float(num_2)
result = "Invalid Operator"

if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == '/':
    result = num_1 / num_2
elif operator == '*':
    result = num_1 * num_2

print(result)