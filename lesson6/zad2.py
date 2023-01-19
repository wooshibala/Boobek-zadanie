a = int(input())
b = int(input())
numbers = [x for x in range(a, b+1) if x % 3 == 0]
average = sum(numbers) / len(numbers)
print(average)
