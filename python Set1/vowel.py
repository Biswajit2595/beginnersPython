# Input string
input_string = "Hello"

# Convert the input string to lowercase (optional for case-insensitive count)
input_string = input_string.lower()

# Initialize a variable to count vowels
vowel_count = 0

# Define a set of vowels
vowels = "aeiou"

# Loop through each character in the input string
for char in input_string:
    # Check if the character is a vowel
    if char in vowels:
        vowel_count += 1

# Print the count of vowels
print(f"Number of vowels: {vowel_count}")
