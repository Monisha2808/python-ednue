#input

name=input("Enter your name:")
rollNo=input("Enter your roll no:")

# output

print(f"My name is {name} and my rollNumber is {rollNo}")

# to get multiple inputs in a single input commands

numbers=input("Enter multiple numbers using comma separator:")
commaSeparatedNumber=numbers.split(",")
print(commaSeparatedNumber)

# to check the type of the input
numbers=input("Enter something:")
print(type(numbers))
# print(numbers)

# type conversion/casting

score=input("enter score:")
print(type(score))
print("My HSC scor:"+score)
print(100+int(score))