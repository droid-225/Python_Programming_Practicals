age = int(input())
multi = 4

if 18 <= age <= 100:
    print("You can vote!")
elif age > 100:
    print("You should be dead!!!!!!")
elif age <= 0:
    print("LIAR!!!!")
else:
    print("You are not able to vote!")

while multi != 0:
    print("Multiplier = ", multi)
    multi -= 1

for i in range(0, 5):
    print("For loop iteration ", i + 1, " completed")