import math # have to import in order to use math.floor or math.ceil

s1 = "Ault"
s2 = "Kelly"

# Find the middle index of s1
middle_index = len(s1)/2
floor=math.floor(middle_index)

# Create s3 by inserting s2 into s1 at the middle index
s3 = s1[:floor] + s2 + s1[floor:]

print(s3)

