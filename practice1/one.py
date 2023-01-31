count = 0
for i in range(0, 1001):
    if i % 17 == 0:
        count += 1
        print(i)
print("Total number of integers divisible by 17:", count)
