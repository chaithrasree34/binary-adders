# binary-adders
# Python program for binary addition

A = input("Enter first binary number: ")
B = input("Enter second binary number: ")

# Convert binary numbers to decimal
num1 = int(A, 2)
num2 = int(B, 2)

# Add the numbers
sum_result = num1 + num2

# Convert the result back to binary
binary_sum = bin(sum_result)[2:]

print("Binary Sum =", binary_sum)

Example

Input:

Enter first binary number: 1010
Enter second binary number: 0110


Output:

Binary Sum = 10000

Using Full Adder Logic

For a 1-bit full adder:

Sum = A XOR B XOR Carry

Carry = (A AND B) OR (Carry AND (A XOR B))

# Python program for 1-bit Full Adder

A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
Cin = int(input("Enter Carry-in (0 or 1): "))

Sum = A ^ B ^ Cin
Cout = (A & B) | (Cin & (A ^ B))

print("Sum =", Sum)
print("Carry =", Cout)


This second program is useful for Digital Electronics lab experiments on binary adders.
