#Demonstrate Error Handling

try:
    number = int(input("Enter an integer: "))
    print(f"You entered: {number}")
except ValueError:
    print("Error: That's not a valid integer.")