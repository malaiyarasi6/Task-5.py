data = [10, 'hello', 22, 'world', 100, 999, 'python', 351]

# Use lambda function to check the type of each element
result = list(map(lambda x: 'Integer' if isinstance(x, int) else 'String', data))

print(result)