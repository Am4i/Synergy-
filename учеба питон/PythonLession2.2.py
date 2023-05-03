# Request a five-digit integer from the user
num = int(input("Enter a five-digit integer: "))

# Extract the digits from the number
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10

# Calculate the result
result = pow(tens, ones) * (hundreds * 100) / (thousands - thousands * 10)

# Print the result
print("Result:", result)
