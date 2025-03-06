print("Hello, World")

name = "Alice"
age = 36
height = 1.7
is_student = True

print(name, age, height, is_student)

name = input("Enter your name: ")
print("Hello, " +name+ "!")

age = int(input("Enter your age: "))

if age >=18:
    print("You are an adult.")
else:
    print("You are young!")

for i in range(9):
    print("Number", i)

count = 0
while count < 4:
    print("Count:", count)
    count += 1

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")