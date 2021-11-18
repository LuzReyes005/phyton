# Luz Elena Reyes
# Tuesday Nov. 16

y = 6
x = [1,2]

# create list

print("---> Everything in my possesion")

inventory = ["banana","gum","candy","card"]

# print variables

print(y)
print(x)

print(inventory)
print(inventory[2])

# first loop

print("--->Regular loop")

count = 0

while count < 4:
    print(inventory[count])
    count = count + 1

# second loop

print("--->Backward loop")

count = 3

while count > 0:
    print(inventory[count])
    count = count - 1

# for loop

print("--->The invetory for loop")

for count in inventory:
    print(count)
