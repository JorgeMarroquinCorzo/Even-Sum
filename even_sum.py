total = 0
for i in range(1, 51):
    if i % 2 == 0:
        total += i

print("The sum of even numbers from 1 to 50 is", total, ".")

#######################################################################

total_while = 0
i = 1
while i <= 50:
    if i % 2 == 0:
        total_while += i
    i += 1

print("The sum of even numbers from 1 to 50 is", total_while, ".")
