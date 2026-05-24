greetings ="Good MOrning"
name = input("Enter SALUTATION: ")
if greetings =="Morning":
    print(greetings)
else:
    print("HEY")

# FOR LOOP
# A for loop is used to repeat code a fixed number of times
# or to loop through items in a sequence.
obj = [2, 3, 4,5, 7, 8, 9, 10]
for i in obj:
    print(i)

# through a range J = I-1 RANGE(I,J)
for J in range(1,6):
    print(J)

# WHILE LOOP
# A while loop runs as long as a condition is True.

count = 0

while count < 5:
    print(count)
    count += 1

#Breaking a while loop
while True:
    number = int(input("Enter number: "))

    if number == 0:
        break

    print(number)
    
#While in list
numbers = [10, 20, 30]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

