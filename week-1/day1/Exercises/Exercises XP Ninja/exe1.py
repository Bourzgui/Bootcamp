# Expression 1: 3 <= 3 < 9
# This is a chained comparison: checks if 3 is less than or equal to 3 AND 3 is less than 9
print("3 <= 3 < 9:", 3 <= 3 < 9)  # True

# Expression 2: 3 == 3 == 3
# Checks if all values are equal
print("3 == 3 == 3:", 3 == 3 == 3)  # True

# Expression 3: bool(0)
# 0 is considered False in boolean context
print("bool(0):", bool(0))  # False

# Expression 4: bool(5 == "5")
# Comparing int and string, which are never equal in Python
print('bool(5 == "5"):', bool(5 == "5"))  # False

# Expression 5: bool(4 == 4) == bool("4" == "4")
# Both comparisons are True, so their boolean values are equal
print('bool(4 == 4) == bool("4" == "4"):', bool(4 == 4) == bool("4" == "4"))  # True

# Expression 6: bool(bool(None))
# None is False in boolean context, and bool(False) is False
print("bool(bool(None)):", bool(bool(None)))  # False

# Final expressions
x = (1 == True)  # True because 1 is equal to True
y = (1 == False)  # False because 1 is not equal to False
a = True + 4     # 5 because True is treated as 1 in arithmetic
b = False + 10   # 10 because False is treated as 0 in arithmetic

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)