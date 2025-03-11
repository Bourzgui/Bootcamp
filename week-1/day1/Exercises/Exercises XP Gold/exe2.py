  
print("All numbers from 1 to 20:")
for num in range(1, 21):
    print(num, end=" ")
print("\n")

print("Numbers with even indices:")
numbers = list(range(1, 21))  
for i in range(0, len(numbers), 2):   
    print(f"Index {i}: {numbers[i]}", end=" ")